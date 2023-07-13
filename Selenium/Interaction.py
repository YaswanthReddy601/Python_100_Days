from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(service=Service(executable_path=path))
driver.get("https://en.wikipedia.org/wiki/Main_Page")
x = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(x.text)
x.click()x
