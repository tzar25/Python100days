import requests
from datetime import datetime
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = getenv("api_key")
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
location = "46.27532874122125,20.149051212501547"
date = f"/{datetime.now().year}-{datetime.now().month:0>2}-{datetime.now().day:0>2}"

parameters = {
    "key": api_key,
    "unitGroup": "metric",
    "lang": "hu",
    # "include": "days"
}

response = requests.get(url=base_url+location+date, params=parameters).json()

for hour in response["days"]["hours"]:
    if hour["precip"] > 1.0 and hour["precipprob"] > 90:
        print(f'{hour["datetime"]} {hour["precip"]}mm eső várható {hour["precipprob"]}% eséllyel.')

print(response)
