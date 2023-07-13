from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = "C://Development/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options, service=Service(executable_path=path))

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London"
           "%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

#signing in
sign_in_button = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()

email = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")

email.send_keys("yaswanthreddy601@gmail.com")
password.send_keys("Zxyw@9493")
password.send_keys(Keys.ENTER)

#Getting jobs in a list
time.sleep(25)
apply_list = driver.find_elements(By.CLASS_NAME, 'disabled.ember-view.job-card-container__link.job-card-list__title')

#applying jobs by using list's index number
for count in range(0, len(apply_list)):
    try:
        apply_list[count].click()

        #Clinking easy apply button using buttons class name
        time.sleep(5)
        driver.find_element(By.CLASS_NAME,"jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view").click()

        #Clicking next button
        cond = True
        while cond:
            try:
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()
                time.sleep(5)
                #if we gett feedback message then it means we have to give other details to apply for this job, so dtop applying
                if driver.find_element(By.CLASS_NAME, "artdeco-inline-feedback__message").is_displayed():
                    cond = False
            #when we check for the feedback message if there is no feedback then we get NoSuchException
            except NoSuchElementException as e:
                print("No Feedback message.")
        #clicking X(cancle) button to close the window and conforming it
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-"
                                           "button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view").click()
        driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco"
                                           "-button--secondary.ember-view").click()
    #If we didnt get the apply button in line 38 then we are going back and apply for the next job
    except NoSuchElementException as e:
        print("Already applied.")
        continue

time.sleep(5)
driver.quit()