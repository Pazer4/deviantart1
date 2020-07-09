from selenium import webdriver
from selenium_function import *


def func_login(login_entry, password_entry):
    # Получает данные логина и пароля
    login = login_entry.get()
    password = password_entry.get()

    # Полученные данные записывает в файл
    file = open("авторизация.txt", "w+")
    file.write("login:" + login + "\n")
    file.write("password:" + password)


def func_list_group(combo):
    browser = webdriver.Chrome()

    # Получает данные о том,с какой вкладки собирать список групп и собирает список групп.
    flag = combo.get()
    groups = list_of_group(browser, flag)
    browser.quit()

    # Записывает полученные данные в файл
    file = open("Список_групп.txt", "w+")
    for group in groups:
        file.write(group + ":" + groups[group] + "\n")
    file.close()


def func_album_group():
    browser = webdriver.Chrome()

    # Берутся даныне авторизации из папки и проивзодит авторизацию.
    file = open("авторизация.txt", "r")
    login = file.readline()[6:]
    password = file.readline()[9:]
    file.close()
    authentication(browser, login, password)

    # Берутся URL сайтов из папки.
    file = open("Список_групп.txt", "r")
    link = []
    stroka = ""
    flag = 0
    for i in file:
        flag2 = 0
        for j in i:
            if (flag == 1 & flag2 == 1):
                stroka += j
            if j == ":":
                flag = 1
                flag2 = 1
        link += [stroka]
        stroka = ""

    # собирается альбомы групп
    dict_album = {}
    for i in link:
        album_of_group(browser, dict_album, i)
    browser.quit()

    # записывает в файл полученный результат
    file = open("анализ_груп.txt", "w+")
    for group in dict_album:
        file.write(group[0:-1] + "=>")
        for album in dict_album[group]:
            file.write(album + "<>")
        file.write("\n")
    file.close()

def func_picture_in_album(file_entry):
    login = "lPazerl"
    password = "A546456A"
    name_picture = file_entry.get()
    link = "https://www.deviantart.com/new-test876578"
    name_album = "test"
    browser = webdriver.Chrome()
    authentication(browser, login, password)
    picture_in_album(browser, link, name_album, name_picture)
    browser.quit()
