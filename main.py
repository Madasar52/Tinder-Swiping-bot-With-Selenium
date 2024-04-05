import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")

time.sleep(3)
login = driver.find_element(By.LINK_TEXT, value="Log in")
login.click()

time.sleep(3)
login = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Log in with phone number"]')
login.click()

time.sleep(3)
phone_number = driver.find_element(By.CSS_SELECTOR, value='input[name="phone_number"]')
phone_number.send_keys(os.environ.get("number"), Keys.ENTER)

location_allow = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(3)

notification_enable = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div/div/div[3]/button[2]')
notification_enable.click()
time.sleep(3)

i_accept = driver.find_element_by_xpath('//*[@id="t-1147506855"]/div/div[2]/div/div/div[1]/button')
i_accept.click()
time.sleep(3)

no_thanks = driver.find_element_by_xpath('//*[@id="t--892698949"]/div/div/div[1]/button')
no_thanks.click()
time.sleep(3)



