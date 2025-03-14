import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def shop_buttons():
    return driver.find_elements(By.CSS_SELECTOR, value="#store > div")


def current_cookies():
    return int(driver.find_element(By.CSS_SELECTOR, value="#money").text.replace(",", ""))


def collect_prices():
    _result = []
    _store = driver.find_element(By.CSS_SELECTOR, value="#store")
    _prices = _store.find_elements(By.CSS_SELECTOR, value="b")

    for price_ in _prices:
        _actual_price = ""
        for char in price_.text:
            if char in "0123456789":
                _actual_price += char
        try:
            _result.append(int(_actual_price))
        except ValueError:
            continue
    return _result


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

timer = time.time() + 5
stopper = time.time() + 300
increment = .5

# TODO refactor the process to not use repetition and be more efficient
while True:
    for _ in range(100):
        cookie.click()
    if time.time() > timer:
        idx = -1
        for price in collect_prices():
            if price <= current_cookies():
                idx = collect_prices().index(price)
        if idx == -1:
            continue
        try:
            while idx > -1:
                while current_cookies() >= collect_prices()[idx]:
                    shop_buttons()[idx].click()
                idx -= 1
        except selenium.common.exceptions.StaleElementReferenceException:
            continue

        timer = time.time() + 5 + increment
        increment += .5

    if time.time() > stopper:
        idx = -1
        for price in collect_prices():
            if price <= current_cookies():
                idx = collect_prices().index(price)
        if idx == -1:
            continue
        try:
            while idx > -1:
                while current_cookies() >= collect_prices()[idx]:
                    shop_buttons()[idx].click()
                idx -= 1
        except selenium.common.exceptions.StaleElementReferenceException:
            continue

        cookies_per_sec = float(driver.find_element(By.CSS_SELECTOR, value="#cps").text.split(" : ")[1].strip())
        print(f"CPS: {cookies_per_sec}")
        break

driver.close()
