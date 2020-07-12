from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import math

# нужен для слежения на какой страницы находимся в программе
flag = 0

# определяет была ли найдена группировка в файле или нет(используется в функции func_select)
flag_3 = 0

# альбом,куда временно сохраняются все выборы по альбомам
dict_group_album = {}


# Сохраняет текущие воборы альбомов в словарь + записывает все из словаря в файл
def save():
    global dict_group_album

    # Проверяет какие группы "активны" и сохраняет выбранный альбом в словарь
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

    # флаг для проверки есть ли такая групировка в файле
    flag_save = 0

    # собирает строку из значений в словаре по принципу:
    # [название группировки] => название группы::название альбома<>название группы::название альбома<>....
    our_string = (select_group_label["text"] + "=>")
    for key in dict_group_album.keys():
        our_string += (key + "::" + dict_group_album[key] + "<>")
    our_string += "\n"

    # Проверяет,есть ли такое название альбома в файле.Если есть,переписывает эту строчку.Если нет,то записывает в конец.
    file_string = open("групировки_альбомов2.txt").readlines()
    file_write = open("групировки_альбомов2.txt", "w")
    for stroka in file_string:
        if stroka.split("=>")[0] == select_group_label["text"]:
            file_write.writelines(our_string)
            flag_save = 1
        else:
            file_write.writelines(stroka)

    if flag_save == 0:
        file_write.writelines(our_string)

    file_write.close()


# проверяет есть ли подстрока(название группировки) в массиве названий альбомов.Если нет,то возвращает СТРОКУ "None"
def substring(substring, values):
    for album in values:
        if substring.lower() in album.lower():
            return album
    return "None"


# Удаляет название группировки из окошка проги и файла с названиями группировок
def delete():
    selection = languages_listbox.curselection()

    # удаляет строку с названием из файла
    text_file = open("групировки_альбомов.txt").readlines()
    delete_file = open("групировки_альбомов.txt", "w")
    for line in text_file:
        if line != languages_listbox.get(selection[0]):
            delete_file.writelines(line)
        else:
            continue
    delete_file.close()

    # удаляет строку из окошка программы
    languages_listbox.delete(selection[0])


# добавление нового названия группировки в окошко и в файл
def add():
    new_language = language_entry.get()
    # добавление в окно программы
    languages_listbox.insert(END, new_language)
    # добавление в файл
    add_file = open("групировки_альбомов.txt", "a")
    add_file.writelines(new_language + "\n")
    add_file.close()


# функция сохраняет в словарь текущие выбранные альбомы групп и "перелистывает" страницу с группами
def func_next(index_flag):
    # флаг следит за номером страницы
    global flag
    flag += index_flag

    # сохраняем текущие выбранные альбомы групп в словарь
    func_save_in_massiv()

    # замена всех label и combo на значения с новой страницы
    # Так же проверяет существует ли вообще группа с таким номером в массиве.Если не существует,то блокирует label и combo
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

    # выставляет значения в combo по текущей группировке
    func_select(0)

    # меняет номер страницы в проге
    label_index.configure(text=str(flag + 1) + "/" + str(math.ceil(more_line / 12)))

    # проверяет должна ли быть активная кнопка next и back
    if (flag + 1) == (math.ceil(more_line / 12)):
        next_button.configure(state="disabled")
    else:
        next_button.configure(state="normal")

    if flag == 0:
        back_button.configure(state="disabled")
    else:
        back_button.configure(state="normal")


# Если label не заблакирован,то добавления выбранное значения с его combo в словарь
def func_save_in_massiv():
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


# Функция обнуляет или заполняет значениями из файла словарь и выставляет нужные значения в combo
def func_select(flag_2):
    # flag_2 определяет была ли нажата кнопка "выбрать" и надо обрабатывать словарь или надо просто выбрать значения в combo.
    global dict_group_album
    global flag_3

    if flag_2 == 1:
        dict_group_album = {}

        index_select_group = languages_listbox.curselection()
        next_button.configure(state="normal")
        select_group = languages_listbox.get(index_select_group)
        select_group_label.configure(text=select_group)

        # проверяет есть ли в файле такая группировка,если есть,то заполняет словарь значениями из файла
        file_select = open("групировки_альбомов2.txt").readlines()
        for i in file_select:
            file_split1 = i.split("=>")
            name = file_split1[0]
            if name == select_group:
                flag_3 = 1
                file_split2 = file_split1[1].split("<>")
                for j in file_split2[0:-1]:
                    file_split3 = j.split("::")
                    dict_group_album[file_split3[0]] = file_split3[1]

    # берёт значения выбранной группы из select_group_label(сделано для безопасности)
    if flag_2 == 0:
        select_group = select_group_label["text"]

    # Проверяет была ли найдена строчка в файле(flag_3=1) и выставляет значение в combo.
    # Если была найдена строчка в файле,то берёт значения из словаря.Если нет,то ищет по названию группировки.
    if flag_3 == 0:
        using_string = substring(select_group, combo_1["values"])
    else:
        using_string = dict_group_album[label_1["text"]]
    index = combo_1["values"].index(using_string)
    combo_1.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_2["values"])
    else:
        using_string = dict_group_album[label_2["text"]]
    index = combo_2["values"].index(using_string)
    combo_2.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_3["values"])
    else:
        using_string = dict_group_album[label_3["text"]]
    index = combo_3["values"].index(using_string)
    combo_3.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_4["values"])
    else:
        using_string = dict_group_album[label_4["text"]]
    index = combo_4["values"].index(using_string)
    combo_4.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_5["values"])
    else:
        using_string = dict_group_album[label_5["text"]]
    index = combo_5["values"].index(using_string)
    combo_5.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_6["values"])
    else:
        using_string = dict_group_album[label_6["text"]]
    index = combo_6["values"].index(using_string)
    combo_6.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_7["values"])
    else:
        using_string = dict_group_album[label_7["text"]]
    index = combo_7["values"].index(using_string)
    combo_7.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_8["values"])
    else:
        using_string = dict_group_album[label_8["text"]]
    index = combo_8["values"].index(using_string)
    combo_8.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_9["values"])
    else:
        using_string = dict_group_album[label_9["text"]]
    index = combo_9["values"].index(using_string)
    combo_9.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_10["values"])
    else:
        using_string = dict_group_album[label_10["text"]]
    index = combo_10["values"].index(using_string)
    combo_10.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_11["values"])
    else:
        using_string = dict_group_album[label_11["text"]]
    index = combo_11["values"].index(using_string)
    combo_11.current(index)

    if flag_3 == 0:
        using_string = substring(select_group, combo_12["values"])
    else:
        using_string = dict_group_album[label_12["text"]]
    index = combo_12["values"].index(using_string)
    combo_12.current(index)


# создание основного окна
new_window = Tk()
new_window.geometry("700x220")
new_window.resizable(False, False)
new_window.title("GUI на Python")

# создание пустых label для выравнивания ширины будущих combo и label
label_empty1 = Label(new_window, width=15).grid(row=0, column=2)
label_empty2 = Label(new_window, width=15).grid(row=0, column=3)
label_empty3 = Label(new_window, width=15).grid(row=0, column=4)

# место ввода названия группировки для добавления
language_entry = Entry(width=30)
language_entry.grid(column=0, row=0, padx=6, pady=6)

# список группировок
languages_listbox = Listbox(width=30, height=4)
languages_listbox.grid(row=1, column=0)

# строка,где пишется название выбранной группы
select_group_label = Label(new_window)
select_group_label.grid(row=2, column=0)

# смотрит есть ли файл с группировками и добавлет группировки в список. Если файла нет,то создает его
try:
    file = open("групировки_альбомов.txt").read().splitlines()
    for i in file:
        languages_listbox.insert(END, i)
except FileNotFoundError:
    file = open("групировки_альбомов.txt", "w+")
    file.close()

# кнопка добавления новой группировки
add_button = Button(text="Добавить", command=add).grid(column=1, row=0)
# кнопка удаления группировки
delete_button = Button(text="Удалить", command=delete).grid(row=1, column=1, sticky=S + W)
# кнопка сохранения выбранных альбомов
save_button = Button(text="Сохранить", command=save).grid(row=2, column=1)
# кнопка выбора группировки
select_button = Button(text="Выбрать", command=lambda: func_select(1)).grid(row=1, column=1, sticky=N)

# проверяет файл "анализ_групп" и добавляет значения от туда в массивы name_group и name_album.
# Если файла не существует,то вылезает окно с предупреждением и закрывется программа
try:
    file = open("анализ_груп.txt", "r").readlines()
    name_group = []
    name_album = []
    more_line = len(file)
    for line in file:
        i = line.split("=>")
        j = ["None"] + i[1].split("<>")
        name_group += [i[0]]
        name_album += [j]
except FileNotFoundError:
    messagebox.showinfo('Атятя', 'Не существует файла с анализом групп')
    sys.exit()

# строка,показывающая номер "страницы"
label_index = Label(new_window, text=str(flag + 1) + "/" + str(math.ceil(more_line / 12)))
label_index.grid(row=6, column=4, sticky=W)

# кнопки для перелистывания "страниц"
back_button = Button(text="Back", state="disabled", command=lambda: func_next(-1))
back_button.grid(row=6, column=4)
next_button = Button(text="Next", state="disabled", command=lambda: func_next(1))
next_button.grid(row=6, column=4, sticky=E)

# создание label и combo для каждой группы
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
