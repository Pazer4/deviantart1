from selenium import webdriver
from selenium_function import authentication
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

triger_name="ONE_ALBUM"
name_picture="1"
link="https://www.deviantart.com/new-test876578"
name_album="test:ONE_ALBUM"

login="lPazerl"
password="A546456A"
browser = webdriver.Chrome()
authentication(browser, login, password)

browser.get(link + "/gallery/")

contribute_button = browser.find_element_by_css_selector("#gmi-GalleryEditor .gmbutton2")
contribute_button.click()

if triger_name not in name_album:
    select_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select_pager")))
    select_button.click()
    select = browser.find_element_by_xpath("//div[text()=\"" + name_album + "\"]")
    select.click()

print("#modalspace [alt^=\'" + name_picture + "\']")
picture=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#modalspace [alt^=\'" + name_picture + "\']")))
picture.click()