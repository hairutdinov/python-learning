import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count_a_tag = driver.find_element(By.CSS_SELECTOR, '#articlecount > a')
# article_count = article_count_a_tag.text
# article_count_a_tag.click()

# all_portals = driver.find_element(By.LINK_TEXT, 'English')
# all_portals.click()

search_input = driver.find_element(By.NAME, 'search')
search_input.send_keys('Python')
search_input.send_keys(Keys.ENTER)

time.sleep(1)

driver.quit()