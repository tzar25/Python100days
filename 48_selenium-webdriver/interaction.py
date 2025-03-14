from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

elem = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(elem.text)
# elem.click()

# Click on a link after finding it via text
# driver.find_element(By.LINK_TEXT, value="Content portals").click()

search_icon = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
search_icon.click()
search_box = driver.find_element(By.CSS_SELECTOR, value='#searchform input')
search_box.send_keys("Python", Keys.ENTER)
