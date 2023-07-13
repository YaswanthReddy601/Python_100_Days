import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C:\Development\chromedriver.exe"

optioins = webdriver.ChromeOptions()
optioins.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=optioins, service=Service(executable_path=path))
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#scrapping the data
cookie = driver.find_element(By.ID, "cookie")

buy_curser = driver.find_element(By.ID, "buyCursor")
buy_grand_ma = driver.find_element(By.ID, "buyGrandma")
buy_Factory = driver.find_element(By.ID, "buyFactory")
buy_Mine = driver.find_element(By.ID, "buyMine")
buy_Shipment = driver.find_element(By.ID, "buyShipment")
buy_Alchemy = driver.find_element(By.ID, "buyAlchemy lab")
buy_Portal = driver.find_element(By.ID, "buyPortal")
buy_TimeMachine = driver.find_element(By.ID, "buyTime machine")


#Getting time in seconds
start_time = int(time.time())

#started clicking the cookie
while True:
    cookie.click()
    end_time = int(time.time())
    #Checking the time to pause the for 5 seconds
    if abs(start_time-end_time) == 5:

        #scrapping the amount of money we have
        money_code = driver.find_element(By.ID, "money")
        money = money_code.text
        #converting into integer
        money = int(money.replace(",", ""))
        print(money)
        time.sleep(5)

        #Checking if we can buy any item or not
        # if money > 123456789:
        #     buy_TimeMachine.click()
        # elif money > 100000:
        #     buy_Portal.click()
        # elif money > 50000:
        #     buy_Alchemy.click()
        # elif money > 7000:
        #     buy_Shipment.click()
        # elif money > 2000:
        #     buy_Mine.click()
        # elif money > 500:
        #     buy_Factory.click()
        # elif money > 100:
        #     buy_grand_ma.click()
        # elif money > 15:
        #     buy_curser.click()
        #pausing the game for 5 seconds

        #Reassigning the start time
        start_time = int(time.time())









