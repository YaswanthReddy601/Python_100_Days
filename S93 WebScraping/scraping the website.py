import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



response= requests.get("https://www.alibaba.com/trade/search?tab=all&searchText=eletronic+bikes")
all_code= response.text
soup= BeautifulSoup(all_code, "html.parser")

#Scraping the data
names= soup.select(".large")
products= [name.text for name in names]
print(products)

prices= soup.select(".elements-offer-price-normal__price")
costs=[prices.text for prices in prices]

quantity= soup.select(".element-offer-minorder-normal__value")
stock= [x.text for x in quantity]

#creating webs=driver
options= webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options, service=Service(executable_path="C://Development/chromedriver.exe"))

#Entering the data to the
driver.get("https://forms.gle/gZ8PV69CL3JZ8thSA")
for x in range(0, len(products)):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(products[x])
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(costs[x])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(stock[x])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Submit another response').click()

driver.quit()