import requests
from datetime import datetime

MY_LNG = 20.149963029980906
MY_LAT = 46.27534790463313

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data['iss_position']['latitude'], data['iss_position']['longitude'])

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LNG}
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
response.raise_for_status()
data = response.json()['results']
sun = int(data['sunrise'][11:13]), int(data['sunset'][11:13])
time_now = datetime.now()

print(time_now.hour)
print(sun)

