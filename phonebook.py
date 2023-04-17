# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
from prettytable import PrettyTable


FILE_PATH = "phonebook.txt"

def read_file():
    info_table = PrettyTable()
    info_table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    with open(FILE_PATH, 'r') as f:
        for line in f:
            info_table.add_row(line.strip().split())
    print(info_table)

def write_file():
    with open(FILE_PATH, 'a') as f:
        f.write(input("Введите данные: " + '\n'))

def find_info():
    find = input("Введите кого нужно найти: ")
    found_entries = []

    with open(FILE_PATH, 'r') as f:
        for line in f:
            if find.casefold() in line.casefold():
                found_entries.append(line)
    if len(found_entries) >= 1:
        print(*found_entries)
    else:
        print("Нет записей, удовлетворяющих поиску")

def delete_info():
    find = input("Введите кого нужно удалить: ")
    phonebook_list = copy_phonebook()
    found_entries = []
    for info_line in phonebook_list:
        if find.casefold() in " ".join(info_line).casefold():
            found_entries.append(info_line)
    if not found_entries:
        print("Нет записей, удовлетворяющих поиску")
        return
    print("Найдены следующие записи:")
    for entry in found_entries:
        print(entry)
        if input("Это нужно удалить? Да/Нет: ").casefold() == 'да'.casefold():
            for i in range(len(entry)):
                entry.pop()
    phonebook_list = [i for i in phonebook_list if i]
    with open(FILE_PATH, 'w') as f:
        for info_line in phonebook_list:
            f.write(" ".join(info_line) + "\n")


def change_info():
    find = input("Введите кого нужно найти: ")
    phonebook_list = copy_phonebook()
    found_entries = []
    for info_line in phonebook_list:
        if find.casefold() in " ".join(info_line).casefold():
            found_entries.append(info_line)
    if not found_entries:
        print("Нет записей, удовлетворяющих поиску")
        return
    print("Найдены следующие записи:")
    for entry in found_entries:
        print(entry)
        if input("Это нужно изменить? Да/Нет: ").casefold() == 'да'.casefold():
            for i, item in enumerate(entry):
                print(item)
                if input("Это нужно изменить? Да/Нет: ").casefold() == 'да'.casefold():
                    change = input("Введите на что нужно заменить: ")
                    entry[i] = change
    with open(FILE_PATH, 'w') as f:
        for info_line in phonebook_list:
            f.write(" ".join(info_line) + "\n")

def copy_phonebook():
    res_list = list()
    with open(FILE_PATH, 'r') as f:
        for line in f:
            res_list.append(line.split())
    return res_list

def hello_menu():
    print("---------------------------------------------------------")
    print("Добро пожаловать в телефонный справочник!")
    print("Выберите действие:")
    print("Вывести все контакты телефонного справочника - 1")
    print("Добавить данные в справочник - 2")
    print("Найти кого-то в справочнике - 3")
    print("Удалить кого-то из справочника - 4")
    print("Изменить чьи-то данные в справочнике - 5")
    print("Завершить работу справочника - 6")
    print("Напечатать варианты действий снова - 7")
    print("---------------------------------------------------------")


flag = True
hello_menu()

while flag:
    choosen_mode = int(input("Введите номер режима: "))
    print("***                                                   ***")
    if choosen_mode == 1:
        read_file()
    elif choosen_mode == 2:
        print("Вводите данные в формате: Фамилия, Имя, Отчество, Номер Телефона")
        write_file()
    elif choosen_mode == 3:
        find_info()
    elif choosen_mode == 4:
        delete_info()
    elif choosen_mode == 5:
        change_info()
    elif choosen_mode == 6:
        print("Пока!")
        flag = False
    elif choosen_mode == 7:
        hello_menu()
        
