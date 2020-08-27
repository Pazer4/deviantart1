from selenium import webdriver
from selenium_function import authentication
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

login="locelotkal"
password="A050699a"
browser = webdriver.Chrome()
authentication(browser, login, password)

link="https://www.deviantart.com/notifications/feedback/activity"
browser.get(link)
users = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._1J4D2 ._29EHf:nth-child(1)")))

users_name=[]
users_id=[]

for user in users:
    users_name += [user.get_attribute("data-username")]
    users_id += [user.get_attribute("data-userid")]

print(1)
print(2)