from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math


# Принимает на вход ссылку на группу. Возвращает имя группы
def name_group(link):
    default_link = "https://www.deviantart.com/"
    name = ""
    for i in range(len(link) - len(default_link)):
        name += link[len(default_link) + i]
    return name


# Принимает на вход браузер,логин и пароль. Производит авторизацию в данном браузере
def authentication(browser, login, password):
    link = "https://www.deviantart.com/users/login"
    browser.get(link)

    browser.find_element_by_css_selector("#username").send_keys(login)
    browser.find_element_by_css_selector("#password").send_keys(password)
    browser.find_element_by_css_selector("#loginbutton").click()


# Принимает на вход строчку с цифрами. Возвращает цифры из этой строчки
def digit_in_string(stroka):
    stroka2 = ""
    for i in stroka:
        if i.isdigit():
            stroka2 += i
    return int(stroka2)


# Принимает браузер и flag(равен Group Member или Watching).Возращает словарь со списком групп(название группы:ссылка на группу)
def list_of_group(browser,flag):
    link = "https://www.deviantart.com/locelotkal/about"
    browser.get(link)

    if flag == "group":
        stroka_selector="#group_list_members ._30hmv"
        button_selector="#group_list_members .ucOYB._36ZWN._1SxyW"
        group_selector="._3mZ8d.FnJV9"
    elif flag == "watching":
        stroka_selector="#watching ._30hmv"
        button_selector="#watching .ucOYB._36ZWN._1SxyW"
        group_selector="#watching .user-link._2diFW._2DrVR._1TzPv"

    stroka = browser.find_element_by_css_selector(stroka_selector).text
    value_group = digit_in_string(stroka)
    for i in range(math.ceil((value_group - 15) / 24)):
        more_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
        more_button.click()

    group_list = browser.find_elements_by_css_selector(group_selector)
    group_dict = {}

    for group in group_list:
        group_href = group.get_attribute("href")
        group_dict[name_group(group_href)] = group_href

    browser.quit()
    return group_dict


# Принимает на вход браузер, словарь с альбомами групп(група:[список альбомов группы]) и ссылку на группу.
# Возвращает словарь с альбомами групп,добавив туда альбомы передаваемой группы.
def album_of_group(browser, dict_album, link):
    browser.get(link + "/gallery/")
    contribute_button = browser.find_element_by_css_selector("#gmi-GalleryEditor .gmbutton2")
    contribute_button.click()
    try:
        select_button = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select_pager")))
        select_button.click()
        list_album = browser.find_elements_by_css_selector(".option")
    except:
        dict_album[name_group(link)] = ["НАПИСАТЬ РУЧКАМИ:ONE_ALBUM"]
        return dict_album

    for album in list_album:
        if name_group(link) in dict_album.keys():
            if album.text not in dict_album[name_group(link)]:
                dict_album[name_group(link)] += [album.text]
        else:
            dict_album[name_group(link)] = [album.text]

    return dict_album


# Принимает на вход браузер,ссылку на группу,имя альбома и название картинки.
# Загружает картинку в альбом выбранной группы.
def picture_in_album(browser, link, name_album, name_picture):
    browser.get(link + "/gallery/")

    contribute_button = browser.find_element_by_css_selector("#gmi-GalleryEditor .gmbutton2")
    contribute_button.click()
    select_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select_pager")))
    select_button.click()

    select = browser.find_element_by_xpath("//div[text()=\"" + name_album + "\"]")
    select.click()

    picture = browser.find_element_by_css_selector("#modalspace [alt^=\"" + name_picture + "\"]")
    picture.click()

    submit_button = browser.find_element_by_css_selector(".ok-label")
    submit_button.click()
