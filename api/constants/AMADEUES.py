from pathfindr_assignment.settings import AMADEUS_API_KEY
from pathfindr_assignment.settings import AMADEUS_API_SECRET

import os

# Payload for fetching the token
PAYLOAD = {
    'grant_type': 'client_credentials',
    'client_id': AMADEUS_API_KEY,
    'client_secret': AMADEUS_API_SECRET
}

# Oauth2.0 token issuer url
TOKEN_URL = os.getenv("TOKEN_URL")

# Flight search params
FLIGHT_SEARCH_PARAMS = {
    "originLocationCode": "{ORIGIN}",
    "destinationLocationCode": "{DESTINATION}",
    "departureDate": "{DATE}",
    "adults": "{ADULTS}"
}

# Setting the amadeues flight search api based on DEV_PROFILE
if os.getenv("DEV_PROFILE") == "TEST":
    API_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
elif os.getenv("DEV_PROFILE") == "PROD":
    # todo: add amadeus production api
    pass
else:
    # defaults to test api
    API_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"