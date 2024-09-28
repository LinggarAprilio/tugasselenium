#Source Code testing Selenium By Linggar Aprilio Khairul Insani TAK Batch 7 QA Engineer

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Inisiasi faker untuk kebutuhan generate random text
fake = Faker()

def generate_random_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    return {
        'Email': email,
        'Password': password,
    }

def fill_form(data):
    driver = webdriver.Chrome(options = options)

    try:
        # Url Access
        driver.get('https://demowebshop.tricentis.com/')

        # Personal data
        driver.find_element(By.CSS_SELECTOR, '.ico-login').click()
        driver.find_element(By.CSS_SELECTOR, '#Email').send_keys(data['Email'])
        driver.find_element(By.CSS_SELECTOR, '#Password').send_keys(data['Password'])
        driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()
        
        time.sleep(5)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    random_data = generate_random_data()
    print(random_data)
    fill_form(random_data)