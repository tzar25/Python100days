import requests
import pandas as pd
import smtplib
from datetime import date, timedelta
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

ALPHA_VANTAGE_API_KEY = getenv("ALPHA_VANTAGE_API_KEY")
NEWSAPI_API_KEY = getenv("NEWSAPI_API_KEY")
MY_EMAIL = getenv("MY_EMAIL")
MY_PW = getenv("MY_PW")

TARGET = getenv("TARGET")

def yesterday(day: date) -> date:
    day_offsets = 3, 1, 1, 1, 1, 1, 2
    return day - timedelta(days=day_offsets[day.weekday()])


def get_stocks_from_csv() -> dict:
    data_csv = pd.read_csv("stock_data.csv", delimiter=",")
    return dict(zip(data_csv.Name, data_csv.Code))


def get_stock_data(symbol: str) -> dict:
    stock_api_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    stock_api = "https://www.alphavantage.co/query"
    return requests.get(url=stock_api, params=stock_api_params).json()


def get_news(stock_name: str) -> dict:
    newsapi_params = {
        "q": stock_name,
        "language": "en",
        "searchIn": "title,description",
        "sortBy": "relevancy",
        "apiKey": NEWSAPI_API_KEY
    }
    newsapi_url = "https://newsapi.org/v2/everything"
    return requests.get(newsapi_url, params=newsapi_params).json()


def send_notification(stock_data: dict) -> None:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PW)

        subject = "Subject:"
        message = ""
        for _, data_dict in stock_data.items():
            subject += f"{data_dict[1]}"
            if data_dict[3]/data_dict[2] > 1:
                subject += "^"
            else:
                subject += "v"
            subject += f"{abs(data_dict[3]/data_dict[2]*100 - 100):.2f}%, "
            message += f"{data_dict[0]} news:\n\n"
            all_news = get_news(data_dict[0])
            for i in range(3):
                # message += all_news["articles"][i]["title"] + "\n"
                message += all_news["articles"][i]["url"] + "\n\n"
            message += "\n=============================\n"

        text = subject[:-2] + "\n\n" + message

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TARGET,
                            msg=text)


watched_stocks = get_stocks_from_csv()
notifications = {}
for name, code in watched_stocks.items():
    data = get_stock_data(code)
    day2 = yesterday(date.today())
    day1 = yesterday(day2)
    start = float(data["Time Series (Daily)"][f"{day1}"]["4. close"])
    end = float(data["Time Series (Daily)"][f"{day2}"]["4. close"])
    quotient = end / start
    if not 0.95 < quotient < 1.05:
        notifications[f"{name}"] = [name, code, start, end]
    print(name, code, start, end, end/start-1, sep="; ")

send_notification(notifications)
