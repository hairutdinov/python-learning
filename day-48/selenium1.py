from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'http://secure-retreat-92358.herokuapp.com'

driver = webdriver.Chrome()

driver.get(URL)

first_name_input = driver.find_element(by=By.NAME, value='fName')
first_name_input.send_keys('Ivan')

last_name_input = driver.find_element(by=By.NAME, value='lName')
last_name_input.send_keys('Ivanov')

email_input = driver.find_element(by=By.NAME, value='email')
email_input.send_keys('ivanov@ivan.com')

sign_up_btn = driver.find_element(by=By.CSS_SELECTOR, value='form button')

sign_up_btn.click()

sleep(5)

driver.quit()