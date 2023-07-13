import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    #To create a selenium driver
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = options, service=Service(executable_path="C://Development/chromedriver.exe"))
        self.Up = 0
        self.Down = 0
        self.promised_Up = 150
        self.promised_Down = 10

    #To get internet speed
    def get_internet_speed(self):
        global Up
        global Down
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(60)
        self.Up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.Down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    #Complaining about internet speed, if it is lessthan the promised speed
    def tweet_at_provider(self):
        time.sleep(2)
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys("yaswanthreddy600@gmail.com")
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys("Yaswanth@123")
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        message = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        if self.Up < self.promised_Up or self.Down < self.promised_Down:
            message.send_keys(f"My internet speed is low {self.Up}/{self.Down}, even though i am paying for high speed internet {self.promised_Up}/{self.promised_Down}")
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]').click()
        time.sleep(5)
        self.driver.quit()

complaint_bot = InternetSpeedTwitterBot()

speed = complaint_bot.get_internet_speed()

twitter = complaint_bot.tweet_at_provider()

