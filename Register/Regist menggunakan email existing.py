#Source Code testing Selenium By Linggar Aprilio Khairul Insani TAK Batch 7 QA Engineer

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://demowebshop.tricentis.com/")
assert "Demo Web Shop" in browser.title

#Skenario Register menggunakan email yang sudah terdaftar

#Your Personal Detail
browser.find_element(By.CSS_SELECTOR, '.ico-register').click()
browser.find_element(By.CSS_SELECTOR, '#gender-male').click()
browser.find_element(By.CSS_SELECTOR, '#FirstName').send_keys('Linggar')
browser.find_element(By.CSS_SELECTOR, '#LastName').send_keys('Aprilio')
browser.find_element(By.CSS_SELECTOR, '#Email').send_keys('linggarTAK@gmail.com')

#Your Password
browser.find_element(By.CSS_SELECTOR, '#Password').send_keys('linggar123')
browser.find_element(By.CSS_SELECTOR, '#ConfirmPassword').send_keys('linggar123')
browser.find_element(By.CSS_SELECTOR, '#register-button').click()

time.sleep(5)

browser.quit()