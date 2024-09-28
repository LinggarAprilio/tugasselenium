#Source Code testing Selenium By Linggar Aprilio Khairul Insani TAK Batch 7 QA Engineer

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Init Generate random used Faker Library
fake = Faker()

def generate_random_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    return {
        'FirstName': first_name,
        'LastName': last_name,
        'Email': email,
        'Password': password,
        'ConfirmPassword': password
    }

def fill_form(data):
    driver = webdriver.Chrome(options = options)

    try:
        # Url Access
        driver.get('https://demowebshop.tricentis.com/')

        # Personal data
        driver.find_element(By.CSS_SELECTOR, '.ico-register').click()
        driver.find_element(By.CSS_SELECTOR, '#gender-male').click()
        driver.find_element(By.CSS_SELECTOR, '#FirstName').send_keys(data['FirstName'])
        driver.find_element(By.CSS_SELECTOR, '#LastName').send_keys(data['LastName'])
        driver.find_element(By.CSS_SELECTOR, '#Email').send_keys(data['Email'])
        driver.find_element(By.CSS_SELECTOR, '#Password').send_keys(data['Password'])
        driver.find_element(By.CSS_SELECTOR, '#ConfirmPassword').send_keys(data['ConfirmPassword'])
        driver.find_element(By.CSS_SELECTOR, '#register-button').click()

        time.sleep(5)

        # Button Submit
        driver.find_element(By.CSS_SELECTOR, 'input[value="Continue"]').click()

        time.sleep(5)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    random_data = generate_random_data()
    print(random_data)
    fill_form(random_data)