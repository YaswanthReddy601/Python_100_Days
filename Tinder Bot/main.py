import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C://Development/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options, service=Service(executable_path=path))

driver.get("https://tinder.com/")

#Clicking login button twice
driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/'
                                       'div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()

time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div[1]/div/div/div[2]/'
                                       'div[2]/span/div[2]/button/div[2]/div[2]/div/span/img').click()

#declining the a permission access
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]').click()

# shifting the windows to login using face book
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]

#switchinf to fB to logingin using facebook credentials
driver.switch_to.window(fb_window)

time.sleep(5)
email_or_number = driver.find_element(By.ID, "email")
email_or_number.send_keys("9966774814")

password = driver.find_element(By.ID, "pass")
password.send_keys("Yaswanth@123")
password.send_keys(Keys.ENTER)

#Switching back to tinder windoe and accepting and declining the location and notifications
driver.switch_to.window(base_window)
try:
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
    driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()

except NoSuchElementException as e:
    print("")

# Swiping left
for x in range(0, 10):
    try:
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button').click()
    except NoSuchElementException as e:
        print(f"{x} a")
#closing the window
time.sleep(15)
driver.quit()

# //*[@id="u490315748"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button====button.Lts($ls-s).Z(0).CenterAlign.Mx(a).Cur(p).Tt(u).Bdrs(50%).P(0).Fw($semibold).focus-button-style.Bxsh($bxsh-btn).Expand.Trstf(e).Trsdu($normal).Wc($transform).Pe(a).Scale(1.1):h.Scale(.9):a.Bgi($g-ds-background-nope):a