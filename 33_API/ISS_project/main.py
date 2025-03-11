import requests
from datetime import datetime
import smtplib
import time
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

TARGET_ADDRESS = getenv("TARGET_ADDRESS")
MY_EMAIL = getenv("MY_EMAIL")
MY_PW = getenv("MY_PW")
MY_LONG = 20.149963029980906
MY_LAT = 46.27534790463313
SMTP = getenv("SMTP")


def send_mail():
    with smtplib.SMTP(SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PW)
        text = ("Subject:ISS visible\n\n The Internation Space Station is near to your location and it is nighttime, "
                "so there is a good chance you could see it if you look up now.")
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TARGET_ADDRESS,
                            msg=text)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# If the ISS is close to my current position,
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        #  ISS is close enough
        if time_now <= sunrise or time_now >= sunset:
            #  It's night
            send_mail()
