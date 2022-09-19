import requests
from requests_oauthlib import OAuth1
import json
from time import sleep

# NOTE: FILL IN THE FOLLOWING VALUES YOURSELF!
# developer.twitter.com
CLIENT_ID = ""
CLIENT_SECRET = ""
TOKEN_KEY = ""
TOKEN_SECRET = ""

# https://api-ninjas.com/api/facts --> sign up
FACT_API_KEY = ""

oauth = OAuth1(CLIENT_ID,
    client_secret=CLIENT_SECRET,
    resource_owner_key=TOKEN_KEY,
    resource_owner_secret=TOKEN_SECRET,
)

while True:
    fact_response = requests.get(
        "https://api.api-ninjas.com/v1/facts",
        headers={"X-Api-Key": FACT_API_KEY},
    )
    fact = fact_response.json()[0]["fact"]

    response = requests.post(
        "https://api.twitter.com/2/tweets",
        auth=oauth,
        json={"text": f"Fun fact that I just came up with myself: {fact}"},
    )

    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

    sleep(30)  # wait 30 seconds so we don't get rate-limited

    

