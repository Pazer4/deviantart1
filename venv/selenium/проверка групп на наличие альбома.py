# Прога проверяет группы только на первой странице. Для полноценной работы надо доработать.
from selenium_import import *

# Начальные данные.
link = "https://groups.deviantart.com/?qh=watchers:b3"
test_slovo = "drag"
number_page_album = 5

# Запускаем браузер и получаем ссылки на группы на этой странице.
browser = webdriver.Chrome()
browser.get(link)
new_list_of_groups = []
list_of_groups = browser.find_elements_by_css_selector("#groupsContent .u.regular")
for group in list_of_groups:
    new_list_of_groups += [group.get_attribute("href")]

# Обробатываем каждую группу.
for group_link in new_list_of_groups:
    # Обрабатываем каждую странице альбома в группе.
    for i in range(number_page_album):
        browser.get(group_link + "gallery/?offset=" + str(i * 10))
        list_of_album = browser.find_elements_by_css_selector("#gmi-DoubleResourceStream .ch-top")
        # Проверка есть ли альбомы на этой странице.
        if not list_of_album:
            break
        else:
            # Обработка названий каждого альбома.
            for album in list_of_album:
                name_album = album.text
                if test_slovo.lower() in name_album.lower():
                    print(group_link, ":", name_album)
