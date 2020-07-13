from window_function import picture_in_album
from selenium import webdriver
from selenium_function import authentication
from window_function import read_login_password


login,password=read_login_password()

name_picture = "1"

grouping_name="test"
dict_album={}
new_dict={}
file=open("групировки_альбомов2.txt").readlines()
for i in file:
    file_split1=i.split("=>")
    if file_split1[0] == grouping_name:
        file_split2=file_split1[1].split("<>")
        for j in file_split2[0:-1]:
            file_split3=j.split("::")
            dict_album[file_split3[0]]=file_split3[1]

for i in dict_album.keys():
    if dict_album[i] != "None":
        file2=open("Список_групп.txt").read().splitlines()
        for j in file2:
            split_group=j.split("::")
            if split_group[0]==i:
                new_dict[dict_album[i]]=split_group[1]

browser = webdriver.Chrome()
authentication(browser, login, password)
for i in new_dict.keys():
    name_album=i
    link=new_dict[i]
    picture_in_album(browser, link, name_album, name_picture)

browser.quit()

'''
link = "https://www.deviantart.com/new-test876578"

name_album = "test"

browser = webdriver.Chrome()
authentication(browser, login, password)
picture_in_album(browser, link, name_album, name_picture)
browser.quit()
'''