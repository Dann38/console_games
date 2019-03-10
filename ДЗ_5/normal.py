# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy as es
import os

answer = 5
place = os.getcwd()

def cls():
    print ("\n" * 20)

def body(num):
    global  place
    if num == 1:
        newplace = input("Введите название папки")
        old = place
        try:
            place = os.path.realpath(newplace)
            es.my_dir(place)
        except:
            place = old
    if num == 2:
        es.my_dir(place)
    if num == 3:
        os.chdir(place)
        name = input("Введите название папки")
        try:
            es.my_rmdir(name)
        except OSError:
            print("СИСТЕМНАЯ ОШИБКА, скорее всего папка содержит файлы")
    if num == 4:
        os.chdir(place)
        name = input("Введите название папки")
        es.my_mkdir(name)

def start():
    global answer
    while True:
        print(
"""+++++++++++++++++++++++++++++++++++++
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
5. Выход
+++++++++++++++++++++++++++++++++++++""")
        answer = input(":")
        cls()
        try:
            answer = int(answer)
            if answer == 5:
                break
            else:
                body(answer)
        except ValueError:
            print("Не коректный запрос")

start()
