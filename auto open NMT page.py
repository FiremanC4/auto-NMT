from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

KEY={
'rnokpp':'1234567890',
'docnumber':'001234567',
}

browser = webdriver.Chrome()
browser.get('https://my.testportal.gov.ua/cabinet/login')
assert 'Кабінет учасника' in browser.title

elem = browser.find_element(By.ID, 'rnokpp')
elem.send_keys(KEY['rnokpp'])

select = Select(browser.find_element(By.ID, 'doctype'))
select.select_by_index(1)

elem = browser.find_element(By.ID, 'docnumber')
elem.send_keys(KEY['docnumber'])

input('press ENTER to exit ')

browser.quit()
