from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

driver.find_element(By.NAME, value="fName").send_keys("Sanyi")
driver.find_element(By.NAME, value="lName").send_keys("Sandorella")
driver.find_element(By.NAME, value="email").send_keys("sanyi.sandorella@nowhere.org")
driver.find_element(By.CSS_SELECTOR, value="html body form button").click()


