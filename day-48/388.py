from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.python.org')

events = []
li_tags = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget ul.menu li')

for li_tag in li_tags:
    time_tag = li_tag.find_element(By.TAG_NAME, 'time')
    datetime = time_tag.get_attribute('datetime')
    event_date = datetime.split('T')[0]
    a_tag = li_tag.find_element(By.TAG_NAME, 'a')
    event_name = a_tag.text
    events.append({
        'time': event_date,
        'name': event_name,
    })

print(events)

driver.quit()