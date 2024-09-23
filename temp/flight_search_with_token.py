import requests

api_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

token = "4JI4fgv5OFxUQItrT4fhZavJezMI"

# Headers with the access token
headers = {
    "Authorization": f"Bearer {token}"
}

params = {
    "originLocationCode": "LON",      # Departure airport (London)
    "destinationLocationCode": "NYC", # Destination airport (New York)
    "departureDate": "2024-10-01",    # Departure date
    "adults":1
}

# Make the API request
response = requests.get(api_url, headers=headers, params=params)

# Parse the response
if response.status_code == 200:
    flight_offers = response.json()
    print(flight_offers.keys())
    print(len(flight_offers))
    for offer in flight_offers['data']:
        print(f"Price: {offer['price']['total']} {offer['price']['currency']}")
else:
    print(f"Failed to fetch flight offers. Status code: {response.status_code}")
    print(response.text)