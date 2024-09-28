from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://demowebshop.tricentis.com/")
assert "Demo Web Shop" in browser.title

#Skenario dimulai dari login dulu

#Login
browser.find_element(By.CSS_SELECTOR, '.ico-login').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '#Email').send_keys('linggarTAK@gmail.com')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '#Password').send_keys('linggar123')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()
time.sleep(2)

#Add to chart salah satu product
browser.find_element(By.XPATH, '//div[@class="product-grid home-page-product-grid"]//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'div#bar-notification > span[title="Close"]').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR,'li#topcartlink  .cart-label').click()
time.sleep(2)

browser.find_element(By.XPATH, '/html//select[@id="CountryId"]/option[text()="Zimbabwe"]').click()
time.sleep(2)
browser.find_element(By.XPATH, '/html//input[@id="termsofservice"]').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'button#checkout').click()
time.sleep(2)

#Checkout Product
#Billing address
time.sleep(2)
browser.find_element(By.XPATH, '/html//input[@id="BillingNewAddress_Company"]').send_keys('Test')
time.sleep(2)
browser.find_element(By.XPATH, '/html//select[@id="BillingNewAddress_CountryId"]/option[text()="Indonesia"]').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'input#BillingNewAddress_City').send_keys('JKT')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'input[name="BillingNewAddress.Address1"]').send_keys('Jakarta kemayoran cibereum')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'input#BillingNewAddress_ZipPostalCode').send_keys('123312')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'input#BillingNewAddress_PhoneNumber').send_keys('0813132138819')
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'div#billing-buttons-container > input[title="Continue"]').click()

 
#shipping address
time.sleep(2)
browser.find_element(By.XPATH, '//div[@id="shipping-buttons-container"]/input[@title="Continue"]').click()

#shipping method
time.sleep(2)
browser.find_element(By.XPATH, '//div[@id="shipping-method-buttons-container"]/input[@value="Continue"]').click()

#Payment method
time.sleep(2)
browser.find_element(By.XPATH, '//div[@id="payment-method-buttons-container"]/input[@value="Continue"]').click()

#Payment information
time.sleep(2)
browser.find_element(By.XPATH,'//div[@id="payment-info-buttons-container"]/input[@value="Continue"]').click()

#Checkout 
time.sleep(2)
browser.find_element(By.XPATH, '//div[@id="confirm-order-buttons-container"]/input[@value="Confirm"]').click()

#Success checkout
time.sleep(2)
browser.find_element(By.XPATH, '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]/div[@class="center-1"]//input[@value="Continue"]').click()

#cek detail orders
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '.header-links > ul  .account').click()
time.sleep(2)
browser.find_element(By.XPATH, '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]//ul[@class="list"]//a[@href="/customer/orders"]').click()
time.sleep(2)
browser.find_element(By.XPATH, '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]/div[@class="center-2"]//input[@value="Details"]').click()
time.sleep(5)

browser.quit()