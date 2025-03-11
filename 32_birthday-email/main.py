import datetime as dt
import smtplib
import random as rd
import pandas as pd
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

MY_EMAIL = getenv("MY_EMAIL")
MY_PW = getenv("MY_PW")
SMTP = getenv("SMTP")


def send_mail(contact_data):
    with smtplib.SMTP(SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PW)
        text = "Subject:Szulinap\n\n"
        with open("wish_texts.txt", 'r') as wishes:
            text += rd.choice(wishes.readlines())
            text = text.replace(" - ", "\n\n")
            text = text.replace("[name]", contact_data['name'])
            text = text.replace("[nth]", f"{now.year - contact_data['year']}.")
            text += "\n\nUdvozlettel,\nSanyi"
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=contact_data["email"],
                            msg=text)


data = pd.read_csv("list.csv")
data_dict = data.to_dict(orient="records")

now = dt.datetime.now()
for contact in data_dict:
    if contact['month'] == now.month and contact['day'] == now.day:
        send_mail(contact)

# could be run e.g. on pythonanywhere.com, or any similar cloud service daily
