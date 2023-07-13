import getpass
import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class InstaFollower:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path="C://Development/chromedriver.exe"))

    #To login
    def login(self):
        self.driver.get("https://www.instagram.com/nirmala_nirmal_100/")
        time.sleep(5)
        login = self.driver.find_element(By.LINK_TEXT, "Log In").click()
        time.sleep(5)
        email = self.driver.find_element(By.NAME, "username")
        email.send_keys("nirmala_nirmal_100")
        # email.send_keys(input("Enter username"))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("Nirmal@123")
        # password.send_keys(getpass.getpass("Enter password"))
        password.send_keys(Keys.ENTER)

    #To find followers
    def find_followers(self):
        time.sleep(15)
        self.driver.find_element(By.TAG_NAME, 'a').click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, '_a9--._a9_1').click()
        time.sleep(10)
        # self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_WV"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div/div/div/div/div[1]/div[1]/a').click()

    #To follow
    def follow(self):
        time.sleep(5)
        accounts_list = self.driver.find_elements(By.CLASS_NAME, "_acan._acap._acas._aj1-")
        count = 0
        #If we click the person, we are already following we will get a popup and gets ElementClickInterceptedException to avoid that we use try except
        try:
            for x in range(0, len(accounts_list)):
                count += 1
                time.sleep(3)
                accounts_list[x].click()
                if count == 9:
                    # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    self.driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
                    count = 0
        except ElementClickInterceptedException  as e:
            self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1")
        finally:
            time.sleep(10)
            self.driver.quit()

bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()

