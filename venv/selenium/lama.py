from selenium import webdriver
from selenium_function import authentication
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


max_user=input("Максимальное число пользователей:")
link="https://www.deviantart.com/notifications/feedback/activity"


login="locelotkal"
password="A050699a"
browser = webdriver.Chrome()
authentication(browser, login, password)

browser.get(link)

users = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._1J4D2 ._29EHf:nth-child(1) > a")))

while len(users) < int(max_user):
    browser.execute_script("return arguments[0].scrollIntoView(true);", users[len(users) - 1])
    users = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._1J4D2 ._29EHf:nth-child(1) > a")))


users_name=[]
users_id=[]
users_class=[]
text=[]

for user in users:
    users_name += [user.get_attribute("data-username")]
    users_id += [user.get_attribute("data-userid")]
    users_class += [user.get_attribute("class")]
    text+=[user.text]

for flag in range(len(users)):
    link=f"https://www.deviantart.com/modal/badge/give?badgetype=llama&originating_message_id=&referrer=https%3A%2F%2Fwww.deviantart.com%2F{users_name[flag]}&to_user={users_id[flag]}&trade_id=0"
    browser.get(link)

    give_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".separated .smbutton")))
    give_button.click()
browser.qute()