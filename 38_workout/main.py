import requests
from datetime import datetime
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

MY_WEIGHT = 87
MY_HEIGHT = 172
MY_AGE = 36
NUTRI_APP_ID = getenv("NUTRI_APP_ID")
NUTRI_APP_KEY = getenv("NUTRI_APP_KEY")
SHEETY_AUTH = getenv("SHEETY_AUTH")

NUTRI_BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_HEADERS = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_APP_KEY
}

SHEETY_BASE_URL = "https://api.sheety.co/a6a6000ca587d793c69152d8948c7b9f/workoutTracking/workouts"
SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTH
}

nutri_params = {
    "query": input("What did you do as exercise? "),
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE}
nutri_response = requests.post(NUTRI_BASE_URL, json=nutri_params, headers=NUTRI_HEADERS).json()
# print(nutri_response)

for exercise in nutri_response['exercises']:
    params = {
        'workout': {
            'date': datetime.now().strftime('%Y/%m/%d'),
            'time': datetime.now().strftime('%H:%M'),
            'exercise': exercise['name'].title(),
            'duration': f"{exercise['duration_min']} minutes",
            'calories': exercise['nf_calories']
        }
    }
    sheety_response = requests.post(SHEETY_BASE_URL, json=params, headers=SHEETY_HEADERS).json()
    # print(sheety_response)
