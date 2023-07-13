import requests
from bs4  import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#connecting to the website
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69234177970014%2C%22north%22%3A37.85814816331502%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
                        , headers=header)
all_code = response.text

soup = BeautifulSoup(all_code, "html.parser")

#Grabing the data
all_Addresses = soup.select("address")
addresses = [each_address.text for each_address in all_Addresses]
print(addresses)

time.sleep(3)
all_prices = soup.select(".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1.iMKTKr")
prices = [each_price.text for each_price in all_prices]
print(prices)

all_links = soup.select(".property-card-link")
links = []
for each_link in all_links:
    link = each_link["href"]
    if "https" not in link:
        links.append(f"https://www.zillow.com{link}")
    else:
        links.append(link)
print(links)

#Creating the webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path="C://Development/chromedriver.exe"))

#Entering the data to the google form
time.sleep(3)
driver.get("https://forms.gle/T4GbnZrMvCamj1zQ7")
for y in range(0, len(addresses)):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addresses[y])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[y])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[y])
    driver.find_element(By.CLASS_NAME, "l4V7wb.Fxmcue").click()
    print("record inserted")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

#quitting/closing the driver
driver.quit()
