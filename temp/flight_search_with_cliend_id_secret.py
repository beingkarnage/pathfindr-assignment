from amadeus import Client, ResponseError

amadeus = Client(
    client_id='8OtPPpNrufKSRZ7F33gbRkinf8L0sjQu',      # Replace with your actual API key
    client_secret='9Pf0oaAEG6nTHDLG'  # Replace with your actual API secret
)

try:
    # Make the API call to search for flight offers
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='LON',   # Departure airport (e.g., London)
        destinationLocationCode='NYC',  # Destination airport (e.g., New York)
        departureDate='2024-10-01',  # Departure date in YYYY-MM-DD format
        adults=1                     # Number of adults traveling
    )

    # Parse the response and print the flight offers
    for offer in response.data:
        print(f"Price: {offer['price']['total']} {offer['price']['currency']}")
        for segment in offer['itineraries'][0]['segments']:
            print(f"Flight from {segment['departure']['iataCode']} to {segment['arrival']['iataCode']}")
            print(f"Airline: {segment['carrierCode']}, Flight Number: {segment['number']}")
            print(f"Departure Time: {segment['departure']['at']}")
            print(f"Arrival Time: {segment['arrival']['at']}")
            print("-" * 40)

except ResponseError as error:
    print(f"An error occurred: {error}")