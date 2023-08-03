import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options, service=Service(executable_path="C://Development/chromedriver.exe"))

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response= requests.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.67365492773438%2C%22east%22%3A-122.19300307226563%2C%22south%22%3A37.61120302656595%2C%22north%22%3A37.93901649663059%7D%2C%22mapZoom%22%3A11%2C%22usersSearchTerm%22%3A%22undefined%22%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
                       , headers=header)
all_code= response.text
soup= BeautifulSoup(all_code, "html.parser")
address= soup.select("address")
address= [each_add.text for each_add in address]
print(address)

rents=soup.select(".iMKTKr")
rents=[each_rent.text for each_rent in rents]
print(rents)

all_links=soup.select(".property-card-link")
links=[]
for each_link in all_links:
    link= each_link["href"]
    if "https" not in link:
        links.append(f"https://www.zillow.com{link}")
    else:
        links.append(link)

driver.get("https://forms.gle/T4GbnZrMvCamj1zQ7")
for x in range(0,len(address)):
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address[x])
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(rents[x])
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[x])
    driver.find_element(By.CLASS_NAME, "l4V7wb.Fxmcue").click()
    print(f"{x+1} house details entered")
    driver.find_element(By.LINK_TEXT, "Submit another response").click()

driver.quit()

