from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B0B8SVGBL4/ref=sr_1_2_sspa?crid=3AK9KVLFMVGO2&keywords=samsung+galaxy+flip&qid=1687953871&sprefix=samsung+galaxy+fli%2Caps%2C249&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# title = driver.find_element(By.ID, "title")
# print(title.text)

# search_engine = driver.find_element(By.NAME, "field-keywords")
# print(search_engine.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "dealBadge")
# print(logo.size)

# xpath_ = driver.find_element(By.XPATH, '//*[@id="feature-bullets"]/ul/li[3]/span')
# print(xpath_.text)

xpath__ = driver.find_element(By.XPATH, '//*[@id="nav-logo-sprites"]')
print(xpath__.get_attribute("href"))


