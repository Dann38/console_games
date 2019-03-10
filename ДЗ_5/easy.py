import os
import shutil

def my_mkdir(name):
    try:
        os.mkdir(name)
        print(f"Папка {name} была создана")
    except FileExistsError:
        print(f"Папка {name} уже существует")


def my_rmdir(name):
    try:
        os.rmdir(name)
        print(f"Файл {name} был удален")
    except FileNotFoundError:
        print(f"Файл {name} не найден")


def my_dir(place=os.getcwd()):
    print("======================================")
    lst = (os.listdir(place))
    lst.sort()
    for ls in lst:
        print(ls)
    print("======================================")


def my_copy(name):
    try:
        shutil.copy(name, f"(copy).{name}")
    except FileNotFoundError:
        print(f"Файл {name} не найден")


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print(__name__)
if __name__ ==  "__main__":
    # ЗАДАЧА 1
    for i in range(9):
        my_mkdir(f"dir_{i + 1}")

    for i in range(9):
        my_rmdir(f"dir_{i + 1}")


    # ЗАДАЧА 2
    my_dir()


    # ЗАДАЧА 3
    my_copy("hard.py")
    os.remove("(copy).hard.py")