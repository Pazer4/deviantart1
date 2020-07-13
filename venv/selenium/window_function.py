from selenium import webdriver
from selenium_function import list_of_group,authentication,album_of_group,picture_in_album
import os

def read_login_password():
    file = open("авторизация.txt", "r").read().splitlines()
    for i in file:
        if "login" in i:
            login = i[6:]
        else:
            password = i[9:]
    return login,password

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
    login,password=read_login_password()
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

def func_picture_in_album(file_entry,grouping_combo):
    login, password = read_login_password()

    name_picture = file_entry.get()

    grouping_name = grouping_combo.get()
    dict_album = {}
    new_dict = {}
    file = open("групировки_альбомов2.txt").readlines()
    for i in file:
        file_split1 = i.split("=>")
        if file_split1[0] == grouping_name:
            file_split2 = file_split1[1].split("<>")
            for j in file_split2[0:-1]:
                file_split3 = j.split("::")
                dict_album[file_split3[0]] = file_split3[1]

    for i in dict_album.keys():
        if dict_album[i] != "None":
            file2 = open("Список_групп.txt").read().splitlines()
            for j in file2:
                split_group = j.split("::")
                if split_group[0] == i:
                    new_dict[dict_album[i]] = split_group[1]

    browser = webdriver.Chrome()
    authentication(browser, login, password)
    for i in new_dict.keys():
        name_album = i
        link = new_dict[i]
        picture_in_album(browser, link, name_album, name_picture)

    browser.quit()

#запускает файл grouping.py
def func_grouping():
    os.system('python grouping.py')