from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/bulat/Development/chromedriver'

driver = webdriver.Chrome()

driver.get('https://www.ozon.ru/product/chelsi-marcelo-merotti-675093905/?avtc=1&avte=2&avts=1687244413&sh=AJiK3B4RIQ')

price_block = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[4]/div[3]/div[3]/div/div[13]/div/div[1]/div/div/div[1]/div[1]/button/span/div/div[1]/div/div/span')
print(price_block)

driver.quit()