import logging
import requests

from api.constants.AMADEUES import PAYLOAD, TOKEN_URL
from api.constants.CACHE import AMADEUS_API_TOKEN_PLACEHOLDER, DEFAULT_REDIS_CACHE_TIMEOUT
from api.caching.caching_service import set_cache

logging.basicConfig(level=logging.INFO)


def refresh_token():
    """
    gets the auth token and sets it to cache
    """
    logging.info("Acquiring new token")
    response = requests.post(TOKEN_URL, data=PAYLOAD)

    try:
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data['access_token']
            set_cache(AMADEUS_API_TOKEN_PLACEHOLDER, access_token, DEFAULT_REDIS_CACHE_TIMEOUT)
            logging.info("New token acquired")
        else:
            logging.info(f"Something went wrong while acquiring the token {response.text}")
            raise ConnectionError("Something went wrong while acquiring the token")
    except Exception as E:
        logging.error(f"Unable to fetch token, Status code: {response.status_code}")
        logging.error(E)
