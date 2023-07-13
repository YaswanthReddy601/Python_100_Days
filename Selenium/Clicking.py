from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C:\Development\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options, service=Service(executable_path=path))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# x = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(x.text)
# # x.click()
#
# hist = driver.find_element(By.LINK_TEXT, "View history")
# # hist.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("wikipediya")
# search.send_keys(Keys.ENTER)
# butn = driver.find_element((By.TAG_NAME, "Button"))
# butn.click()


fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Yaswanth")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Chinna...")
gmail = driver.find_element(By.NAME, "email")
gmail.send_keys("yc@gmail.com")

gmail.send_keys(Keys.ENTER)
