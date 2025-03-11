# motivation sender
import datetime as dt
import smtplib
import random as rd
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

my_email = getenv("my_email")
pw = getenv("my_pw")
target_mail = getenv("target_mail")
SMTP = getenv("SMTP")

now = dt.datetime.now()
if now.weekday() == 4:
    with smtplib.SMTP(SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        message = "Subject:Motivational quote\n\n"
        with open("quotes.txt", "r") as quotes:
            lines = quotes.readlines()
            quote, author = rd.choice(lines).split(" -")
            message += quote + " -- " + author

        connection.sendmail(from_addr=my_email,
                            to_addrs=target_mail,
                            msg=message)
