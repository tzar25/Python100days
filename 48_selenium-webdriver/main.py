from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

xpath = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'

events = driver.find_elements(By.XPATH, value=xpath)
dates, names = [], []

for event in events:
    date = event.find_element(By.XPATH, value="time").get_attribute("datetime")[:10]
    dates.append(date)
    print(date, end=" " * 5)
    name = event.find_element(By.XPATH, value="a").text
    names.append(name)
    print(name)

event_dict = {i: {"Date": dates[i], "Event": names[i]} for i in range(len(dates))}
print(event_dict)

# driver.close()      # .close() for a single tab, .quit() to exit the browser
