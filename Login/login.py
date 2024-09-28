from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://demowebshop.tricentis.com/")
assert "Demo Web Shop" in browser.title

#Skenario Login Normal

browser.find_element(By.CSS_SELECTOR, '.ico-login').click()
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#Email').send_keys('linggarTAK@gmail.com')
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#Password').send_keys('linggar123')
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()
time.sleep(5)

browser.quit()