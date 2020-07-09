from tkinter import *
from tkinter.ttk import Combobox
import math

flag = 0
dict_group_album={}

def save():
    global dict_group_album

    if label_1["state"] == "normal":
        dict_group_album[label_1["text"]] = combo_1.get()
    if label_2["state"] == "normal":
        dict_group_album[label_2["text"]] = combo_2.get()
    if label_3["state"] == "normal":
        dict_group_album[label_3["text"]] = combo_3.get()
    if label_4["state"] == "normal":
        dict_group_album[label_4["text"]] = combo_4.get()
    if label_5["state"] == "normal":
        dict_group_album[label_5["text"]] = combo_5.get()
    if label_6["state"] == "normal":
        dict_group_album[label_6["text"]] = combo_6.get()
    if label_7["state"] == "normal":
        dict_group_album[label_7["text"]] = combo_7.get()
    if label_8["state"] == "normal":
        dict_group_album[label_8["text"]] = combo_8.get()
    if label_9["state"] == "normal":
        dict_group_album[label_9["text"]] = combo_9.get()
    if label_10["state"] == "normal":
        dict_group_album[label_10["text"]] = combo_10.get()
    if label_11["state"] == "normal":
        dict_group_album[label_11["text"]] = combo_11.get()
    if label_12["state"] == "normal":
        dict_group_album[label_12["text"]] = combo_12.get()


    flag_save = 0
    file_string=open("групировки_альбомов2.txt").readlines()

    file=open("групировки_альбомов2.txt","w")
    our_stroka = (select_group_label["text"] + "=>")
    for i in dict_group_album.keys():
        our_stroka += (i + "::" + dict_group_album[i] + "<>")
    our_stroka+="\n"

    for stroka in file_string:
        if stroka.split("=>")[0] == select_group_label["text"]:
            file.writelines(our_stroka)
            flag_save=1
        else:
            file.writelines(stroka)

    if flag_save == 0:
        file.writelines(our_stroka)

def substring(substring, values):
    for i in values:
        if substring.lower() in i.lower():
            return i
    return "None"


def delete():
    selection = languages_listbox.curselection()

    text_file = open("групировки_альбомов.txt").readlines()
    delete_file = open("групировки_альбомов.txt", "w")
    for line in text_file:
        if line != languages_listbox.get(selection[0]):
            delete_file.writelines(line)
        else:
            continue
    delete_file.close()

    languages_listbox.delete(selection[0])


# добавление нового элемента
def add():
    new_language = language_entry.get()
    languages_listbox.insert(END, new_language)
    add_file = open("групировки_альбомов.txt", "a")
    add_file.writelines(new_language+"\n")
    add_file.close()


def func_next(index_flag):
    global flag
    flag += index_flag

    if (0 + flag * 12) < more_line:
        label_1.configure(state="normal")
        combo_1.configure(state="normal")
        label_1.configure(text=name_group[0 + flag * 12])
        combo_1.configure(values=name_album[0 + flag * 12])
    else:
        label_1.configure(state="disabled")
        combo_1.configure(state="disabled")

    if (1 + flag * 12) < more_line:
        label_2.configure(state="normal")
        combo_2.configure(state="normal")
        label_2.configure(text=name_group[1 + flag * 12])
        combo_2.configure(values=name_album[1 + flag * 12])
    else:
        label_2.configure(state="disabled")
        combo_2.configure(state="disabled")

    if (2 + flag * 12) < more_line:
        label_3.configure(state="normal")
        combo_3.configure(state="normal")
        label_3.configure(text=name_group[2 + flag * 12])
        combo_3.configure(values=name_album[2 + flag * 12])
    else:
        label_3.configure(state="disabled")
        combo_3.configure(state="disabled")

    if (3 + flag * 12) < more_line:
        label_4.configure(state="normal")
        combo_4.configure(state="normal")
        label_4.configure(text=name_group[3 + flag * 12])
        combo_4.configure(values=name_album[3 + flag * 12])
    else:
        label_4.configure(state="disabled")
        combo_4.configure(state="disabled")

    if (4 + flag * 12) < more_line:
        label_5.configure(state="normal")
        combo_5.configure(state="normal")
        label_5.configure(text=name_group[4 + flag * 12])
        combo_5.configure(values=name_album[4 + flag * 12])
    else:
        label_5.configure(state="disabled")
        combo_5.configure(state="disabled")

    if (5 + flag * 12) < more_line:
        label_6.configure(state="normal")
        combo_6.configure(state="normal")
        label_6.configure(text=name_group[5 + flag * 12])
        combo_6.configure(values=name_album[5 + flag * 12])
    else:
        label_6.configure(state="disabled")
        combo_6.configure(state="disabled")

    if (6 + flag * 12) < more_line:
        label_7.configure(state="normal")
        combo_7.configure(state="normal")
        label_7.configure(text=name_group[6 + flag * 12])
        combo_7.configure(values=name_album[6 + flag * 12])
    else:
        label_7.configure(state="disabled")
        combo_7.configure(state="disabled")

    if (7 + flag * 12) < more_line:
        label_8.configure(state="normal")
        combo_8.configure(state="normal")
        label_8.configure(text=name_group[7 + flag * 12])
        combo_8.configure(values=name_album[7 + flag * 12])
    else:
        label_8.configure(state="disabled")
        combo_8.configure(state="disabled")

    if (8 + flag * 12) < more_line:
        label_9.configure(state="normal")
        combo_9.configure(state="normal")
        label_9.configure(text=name_group[8 + flag * 12])
        combo_9.configure(values=name_album[8 + flag * 12])
    else:
        label_9.configure(state="disabled")
        combo_9.configure(state="disabled")

    if (9 + flag * 12) < more_line:
        label_10.configure(state="normal")
        combo_10.configure(state="normal")
        label_10.configure(text=name_group[9 + flag * 12])
        combo_10.configure(values=name_album[9 + flag * 12])
    else:
        label_10.configure(state="disabled")
        combo_10.configure(state="disabled")

    if (10 + flag * 12) < more_line:
        label_11.configure(state="normal")
        combo_11.configure(state="normal")
        label_11.configure(text=name_group[10 + flag * 12])
        combo_11.configure(values=name_album[10 + flag * 12])
    else:
        label_11.configure(state="disabled")
        combo_11.configure(state="disabled")

    if (11 + flag * 12) < more_line:
        label_12.configure(state="normal")
        combo_12.configure(state="normal")
        label_12.configure(text=name_group[11 + flag * 12])
        combo_12.configure(values=name_album[11 + flag * 12])
    else:
        label_12.configure(state="disabled")
        combo_12.configure(state="disabled")

    label_index.configure(text=str(flag + 1) + "/" + str(math.ceil(more_line / 12)))

    if (flag + 1) == (math.ceil(more_line / 12)):
        next_button.configure(state="disabled")
    else:
        next_button.configure(state="normal")

    if flag == 0:
        back_button.configure(state="disabled")
    else:
        back_button.configure(state="normal")

    func_select(0)


def func_select(flag_2):
    global dict_group_album
    if flag_2==1:
        dict_group_album={}
        index_select_group = languages_listbox.curselection()
        next_button.configure(state="normal")
        select_group = languages_listbox.get(index_select_group)
        select_group_label.configure(text=select_group)

    if flag_2==0:
        if label_1["state"]=="normal":
            dict_group_album[label_1["text"]]=combo_1.get()
        if label_2["state"] == "normal":
            dict_group_album[label_2["text"]] = combo_2.get()
        if label_3["state"] == "normal":
            dict_group_album[label_3["text"]] = combo_3.get()
        if label_4["state"] == "normal":
            dict_group_album[label_4["text"]] = combo_4.get()
        if label_5["state"] == "normal":
            dict_group_album[label_5["text"]] = combo_5.get()
        if label_6["state"] == "normal":
            dict_group_album[label_6["text"]] = combo_6.get()
        if label_7["state"] == "normal":
            dict_group_album[label_7["text"]] = combo_7.get()
        if label_8["state"] == "normal":
            dict_group_album[label_8["text"]] = combo_8.get()
        if label_9["state"] == "normal":
            dict_group_album[label_9["text"]] = combo_9.get()
        if label_10["state"] == "normal":
            dict_group_album[label_10["text"]] = combo_10.get()
        if label_11["state"] == "normal":
            dict_group_album[label_11["text"]] = combo_11.get()
        if label_12["state"] == "normal":
            dict_group_album[label_12["text"]] = combo_12.get()
        select_group = select_group_label["text"]

    using_string = substring(select_group, combo_1["values"])
    index = combo_1["values"].index(using_string)
    combo_1.current(index)

    using_string = substring(select_group, combo_2["values"])
    index = combo_2["values"].index(using_string)
    combo_2.current(index)

    using_string = substring(select_group, combo_3["values"])
    index = combo_3["values"].index(using_string)
    combo_3.current(index)

    using_string = substring(select_group, combo_4["values"])
    index = combo_4["values"].index(using_string)
    combo_4.current(index)

    using_string = substring(select_group, combo_5["values"])
    index = combo_5["values"].index(using_string)
    combo_5.current(index)

    using_string = substring(select_group, combo_6["values"])
    index = combo_6["values"].index(using_string)
    combo_6.current(index)

    using_string = substring(select_group, combo_7["values"])
    index = combo_7["values"].index(using_string)
    combo_7.current(index)

    using_string = substring(select_group, combo_8["values"])
    index = combo_8["values"].index(using_string)
    combo_8.current(index)

    using_string = substring(select_group, combo_9["values"])
    index = combo_9["values"].index(using_string)
    combo_9.current(index)

    using_string = substring(select_group, combo_10["values"])
    index = combo_10["values"].index(using_string)
    combo_10.current(index)

    using_string = substring(select_group, combo_11["values"])
    index = combo_11["values"].index(using_string)
    combo_11.current(index)

    using_string = substring(select_group, combo_12["values"])
    index = combo_12["values"].index(using_string)
    combo_12.current(index)





new_window = Tk()
new_window.geometry("700x220")
new_window.title("GUI на Python")
label_empty1 = Label(new_window, width=15).grid(row=0, column=2)
label_empty2 = Label(new_window, width=15).grid(row=0, column=3)
label_empty3 = Label(new_window, width=15).grid(row=0, column=4)

language_entry = Entry(width=30)
language_entry.grid(column=0, row=0, padx=6, pady=6)

languages_listbox = Listbox(width=30, height=4)
languages_listbox.grid(row=1, column=0)

select_group_label=Label(new_window)
select_group_label.grid(row=2,column=0)

try:
    file = open("групировки_альбомов.txt").read().splitlines()
    for i in file:
        languages_listbox.insert(END, i)
except FileNotFoundError:
    file = open("групировки_альбомов.txt", "w+")
    file.close()

add_button = Button(text="Добавить", command=add).grid(column=1, row=0)
delete_button = Button(text="Удалить", command=delete).grid(row=1, column=1, sticky=S + W)
save_button= Button(text="Сохранить",command=save).grid(row=2,column=1)
select_button = Button(text="Выбрать", command=lambda: func_select(1)).grid(row=1, column=1, sticky=N)


file = open("анализ_груп.txt", "r").readlines()
name_group = []
name_album = []
more_line = len(file)
for line in file:
    i = line.split("=>")
    j = ["None"] + i[1].split("<>")
    name_group += [i[0]]
    name_album += [j]


label_index = Label(new_window, text=str(flag + 1) + "/" + str(math.ceil(more_line / 12)))
label_index.grid(row=6, column=4, sticky=W)
back_button = Button(text="Back", state="disabled", command=lambda: func_next(-1))
back_button.grid(row=6, column=4)
next_button = Button(text="Next", state="disabled", command=lambda: func_next(1))
next_button.grid(row=6, column=4, sticky=E)

label_1 = Label(new_window, text=name_group[0 + flag * 12])
label_1.grid(row=0, column=2, sticky=W + E)
combo_1 = Combobox(new_window, values=name_album[0 + flag * 12])
combo_1.grid(row=1, column=2, sticky=N)

label_2 = Label(new_window, text=name_group[1 + flag * 12])
label_2.grid(row=0, column=3, sticky=W + E)
combo_2 = Combobox(new_window, values=name_album[1 + flag * 12])
combo_2.grid(row=1, column=3, sticky=N)

label_3 = Label(new_window, text=name_group[2 + flag * 12])
label_3.grid(row=0, column=4, sticky=W + E)
combo_3 = Combobox(new_window, values=name_album[2 + flag * 12])
combo_3.grid(row=1, column=4, sticky=N)

label_4 = Label(new_window, text=name_group[3 + flag * 12])
label_4.grid(row=1, column=2, sticky=W + E)
combo_4 = Combobox(new_window, values=name_album[3 + flag * 12])
combo_4.grid(row=1, column=2, sticky=S)

label_5 = Label(new_window, text=name_group[4 + flag * 12])
label_5.grid(row=1, column=3, sticky=W + E)
combo_5 = Combobox(new_window, values=name_album[4 + flag * 12])
combo_5.grid(row=1, column=3, sticky=S)

label_6 = Label(new_window, text=name_group[5 + flag * 12])
label_6.grid(row=1, column=4, sticky=W + E)
combo_6 = Combobox(new_window, values=name_album[5 + flag * 12])
combo_6.grid(row=1, column=4, sticky=S)

label_7 = Label(new_window, text=name_group[6 + flag * 12])
label_7.grid(row=2, column=2, sticky=W + E)
combo_7 = Combobox(new_window, values=name_album[6 + flag * 12])
combo_7.grid(row=3, column=2)

label_8 = Label(new_window, text=name_group[7 + flag * 12])
label_8.grid(row=2, column=3, sticky=W + E)
combo_8 = Combobox(new_window, values=name_album[7 + flag * 12])
combo_8.grid(row=3, column=3)

label_9 = Label(new_window, text=name_group[8 + flag * 12])
label_9.grid(row=2, column=4, sticky=W + E)
combo_9 = Combobox(new_window, values=name_album[8 + flag * 12])
combo_9.grid(row=3, column=4)

label_10 = Label(new_window, text=name_group[9 + flag * 12])
label_10.grid(row=4, column=2, sticky=W + E)
combo_10 = Combobox(new_window, values=name_album[9 + flag * 12])
combo_10.grid(row=5, column=2)

label_11 = Label(new_window, text=name_group[10 + flag * 12])
label_11.grid(row=4, column=3, sticky=W + E)
combo_11 = Combobox(new_window, values=name_album[10 + flag * 12])
combo_11.grid(row=5, column=3)

label_12 = Label(new_window, text=name_group[11 + flag * 12])
label_12.grid(row=4, column=4, sticky=W + E)
combo_12 = Combobox(new_window, values=name_album[11 + flag * 12])
combo_12.grid(row=5, column=4)

new_window.mainloop()
