import logging
import os

from django.http import JsonResponse

from api.amadeus.amadeus_fetch_flights import fetch_cheapest_flight
from api.constants.CACHE import AMADEUS_API_TOKEN_PLACEHOLDER
from api.constants.AMADEUES import API_URL, FLIGHT_SEARCH_PARAMS
from api.constants.HTTP import HEADERS, NOCACHE
from api.exceptions.amadeus_api_error import AmadeusApiError
from api.exceptions.auth_token_error import AuthTokenError
from api.exceptions.incomplete_query_params_error import IncompleteQueryParams
from api.utils.dict_formatter import dict_formatter
from api.utils.generate_flight_cache_key import generate_flight_cache_key
from api.caching.caching_service import get_cache, set_cache

logging.basicConfig(level=os.getenv("LOG_LEVEL").upper())


def ping(request):
    response = {"data": "pong"}
    return JsonResponse(response)


def flights(request):
    cheapest_flight = {
        "origin": request.GET.get("origin"),
        "destination": request.GET.get("destination"),
        "departure_date": request.GET.get("date")
    }

    try:
        if request.GET.get("origin", None) is None or request.GET.get("destination", None) is None or request.GET.get(
                "date", None) is None:
            raise IncompleteQueryParams(
                {
                    "origin":request.GET.get("origin"),
                    "destination": request.GET.get("destination"),
                    "date": request.GET.get("date"),
                }
            )
    except IncompleteQueryParams:
        logging.warning(f"Invalid Query Parameters {cheapest_flight}")
        return JsonResponse({"data": f"Invalid Query Parameters {cheapest_flight}"})

    flight_search_param = dict_formatter(
        FLIGHT_SEARCH_PARAMS,
        {
            "ORIGIN": request.GET.get("origin"),
            "DESTINATION": request.GET.get("destination"),
            "DATE": request.GET.get("date"),
            "ADULTS": request.GET.get("adults", 1)
        }
    )
    flight_cache_key = generate_flight_cache_key(
        request.GET.get("origin"),
        request.GET.get("destination"),
        request.GET.get("date"),
    )

    token = get_cache(AMADEUS_API_TOKEN_PLACEHOLDER)

    try:
        if not token:
            raise AuthTokenError()
    except AuthTokenError:
        return JsonResponse({"data": "Invalid Token for auth"})

    header = dict_formatter(HEADERS, {"TOKEN": token})

    if request.GET.get(NOCACHE) == "1":
        if get_cache(flight_cache_key):
            # this if-else can be skipped, but just for the logging for capturing hard-refresh events
            logging.info(f"Cache forced refresh : {flight_cache_key}")
            logging.info(f"Re-setting data : {flight_cache_key}")
        else:
            logging.info(f"NOCACHE :Cache miss : {flight_cache_key}")
            logging.info(f"NOCACHE :Setting data : {flight_cache_key}")

    else:
        if get_cache(flight_cache_key):
            logging.info(f"Cache hit : {flight_cache_key}")
            return JsonResponse(get_cache(flight_cache_key))

        logging.info(f"Cache miss : {flight_cache_key}")
        logging.info(f"Setting data : {flight_cache_key}")

    try:
        cheapest_flight['price'] = fetch_cheapest_flight(header, flight_search_param, api_url=API_URL)
    except AmadeusApiError as aApiError:
        logging.error(aApiError)
        cheapest_flight['price'] = "ERROR WHILE CALLING THE API"
        return JsonResponse(cheapest_flight)

    set_cache(flight_cache_key, cheapest_flight)

    return JsonResponse(cheapest_flight)
