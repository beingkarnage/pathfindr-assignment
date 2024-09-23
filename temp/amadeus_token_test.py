import requests
from api.constants.AMADEUES import PAYLOAD, TOKEN_URL

response = requests.post(TOKEN_URL, data=PAYLOAD)

# Parse the response to get the access token
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token. Status code: {response.status_code}")
    print(response.text)
