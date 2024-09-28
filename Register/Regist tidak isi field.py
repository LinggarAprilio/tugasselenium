#Source Code testing Selenium By Linggar Aprilio Khairul Insani TAK Batch 7 QA Engineer

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://demowebshop.tricentis.com/")
assert "Demo Web Shop" in browser.title

#Skenario Register tidak isi semua kolom
browser.find_element(By.CSS_SELECTOR, '.ico-register').click()
browser.find_element(By.CSS_SELECTOR, '#register-button').click()

time.sleep(5)

browser.quit()