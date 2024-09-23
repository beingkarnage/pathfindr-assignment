import requests
import logging
import os

from api.constants.AMADEUES import API_URL
from api.exceptions.amadeus_api_error import AmadeusApiError

logging.basicConfig(level=os.getenv("LOG_LEVEL").upper())


def fetch_cheapest_flight(header, flight_search_param, api_url=API_URL):
    """
    Fetches the cheapest flight, based on a bearer token and flight search params
    Args:
        header: (dict), with `Authorization` key, and value as `Bearer {TOKEN}`
        flight_search_param (dict): for searching flight parameters i.e. `originLocationCode`, `destinationLocationCode`, `departureDate`, `adults`
        api_url: (str) Amadeus flight search api url
    """
    response = requests.get(api_url, headers=header, params=flight_search_param)

    if response.status_code == 200:
        flight_offer = response.json()
        return f"{flight_offer['data'][0]['price']['total']} {flight_offer['data'][0]['price']['currency']}"
    else:
        logging.error(f"Failed to fetch flight offers. Status code: {response.status_code}")
        raise AmadeusApiError({"header": header, "params": flight_search_param})
