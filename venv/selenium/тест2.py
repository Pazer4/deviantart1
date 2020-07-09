from selenium_import import *
from selenium import webdriver
from selenium_function import digit_in_string,name_group
import math



browser=webdriver.Chrome()


link = "https://www.deviantart.com/locelotkal/about"
browser.get(link)

stroka = browser.find_element_by_css_selector("#watching ._30hmv").text
value_group = digit_in_string(stroka)
for i in range(math.ceil((value_group - 15) / 24)):
    more_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#watching .ucOYB._36ZWN._1SxyW")))
    more_button.click()

group_list = browser.find_elements_by_css_selector("#watching .user-link._2diFW._2DrVR._1TzPv")
group_dict = {}

for group in group_list:
    group_href = group.get_attribute("href")
    group_dict[name_group(group_href)] = group_href

for i in group_dict.items():
    print(i)