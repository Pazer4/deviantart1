from tkinter import *
from window_function import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image



window = Tk()
w = window.winfo_screenwidth() # ширина экрана
h = window.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 400 # смещение от середины
h = h - 350
window.geometry('800x600+{}+{}'.format(w, h))
window.resizable(False, False)
window.title("Пробная программа")


background_photo = Image.open("D:/1.png")
image = ImageTk.PhotoImage(background_photo)
background_label = Canvas(window,width=800,height=600)
background_label.pack()
background_label.create_image(500,300,image=image)


try:
    file=open("авторизация.txt","r")
    login=file.readline()[6:]
    password=file.readline()[9:]
except FileNotFoundError:
    login=""
    password=""

login_label=Label(window, text="Login")
login_label.place(x=20,y=3)
login_entry=Entry(window, width=10)
login_entry.place(x=56,y=4)
login_entry.insert(0,login)

password_label=Label(window, text="Password")
password_label.place(x=0,y=28)
password_entry=Entry(window, width=10)
password_entry.place(x=56,y=29)
password_entry.insert(0,password)

file_label=Label(window, text="Загружаемый файл")
file_label.place(x=520, y=130)
file_entry=Entry(window, width=10)
file_entry.place(x=635, y=130)


combo = Combobox(window)
combo['values'] = ("group","watching")
combo.current(0)
combo.place(x=100, y=125, height=30, width=80)


btn_login = Button(window, text="авторизация", bg="pink", fg="brown", command=lambda: func_login(login_entry,password_entry))
btn_login.place(x=10, y=53, height=20, width=100)

btn1 = Button(window, text="Сбор списка групп", bg="pink", fg="brown", command=lambda: func_list_group(combo))
btn1.place(x=70, y=150, height=300, width=150)

btn2 = Button(window, text="Анализ альбомов групп", bg="pink", fg="brown", command=func_album_group)
btn2.place(x=320, y=150, height=300, width=150)

btn3 = Button(window, text="Загрузка в группы", bg="pink", fg="brown", command=lambda: func_picture_in_album(file_entry))
btn3.place(x=570, y=150, height=300, width=150)

btn4 = Button(window, text="Составление групп из альбомов", bg="pink", fg="brown")
btn4.place(x=300, y=50, height=50, width=200)


window.mainloop()