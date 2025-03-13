from bs4 import BeautifulSoup
import requests
from os import getenv
from dotenv import load_dotenv
import smtplib


def send_mail(from_, pw_, to_, text_):
    with smtplib.SMTP(host=SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=from_, password=pw_)
        connection.sendmail(from_addr=from_, to_addrs=to_, msg=text_)


load_dotenv(override=True)

SMTP_ADDRESS = getenv("SMTP_ADDRESS")
EMAIL = getenv("MY_EMAIL")
PW = getenv("MY_PW")
TARGET = getenv("TARGET")

url = "https://www.gemklub.hu/andromeda-11398"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0",
    "Accept-Language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find(name="span", class_="product-price")
price = int(price_tag.text.split()[0].replace(".", ""))

message = f"Subject:Andromeda akcio!\n\nAndromeda's Edge most csak {price} Ft a Gemklubon. {url}"

if price < 25000:
    send_mail(EMAIL, PW, TARGET, message)
