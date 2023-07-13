from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=path))
driver.get("https://www.python.org/")
# time_code = driver.find_element(By.CSS_SELECTOR, ".event-widget time")
name_code = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# time = [time_code[z].text for z in range(4)]
name = [name_code[y].text for y in range(4)]

dicto = {x: {"name": name_code[x].text} for x in range(5)}
print(dicto)


