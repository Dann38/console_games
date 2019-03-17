

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""








import random

class Cart:
    def __init__(self, name):
        self.name = name
        self.str1, self.str2, self.str3, self.str4 = num_cart()
    def print_cart(self):
        print(f"============={self.name}=============")

        print(f'|{"|".join(self.str2)}|')
        print(f'|{"|".join(self.str3)}|')
        print(f'|{"|".join(self.str4)}|')

        print(f"============={'=' * len(self.name)}=============")

def num_cart():

    str1 = []
    for i in range(15):
        a = 1
        while True:
            num = random.randint(1, 90)
            for j in str1:
                if j == num:
                    a = 0
                    continue
            if a == 0:
                a = 1
                continue
            break
        str1.append(num)
    str1.sort()

    for i in range(len(str1)):
        str1[i] = str(str1[i])
        if len(str1[i]) == 1:
            str1[i] += ' '

    third = int(len(str1) / 3)

    str2 = str1[:third]
    str3 = str1[third:third * 2]
    str4 = str1[third * 2:]

    for i in range(5):
        str4.insert(random.randint(0, 4), "  ")
    for i in range(5):
        str2.insert(random.randint(0, 4), "  ")
    for i in range(5):
        str3.insert(random.randint(0, 4), "  ")

    return str1, str2, str3, str4

def start():
    print("""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

============================
|  |  |9 |43|62|  |  |74|90|
|2 |  |27|  |  |75|78|  |82|
|  |41|56|63|  |76|  |  |86| 
============================

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.    
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
======================================================================= 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  
    """)

    you = Cart("DANIIL")
    you.print_cart()
    comp = Cart("Компьютер")
    comp.print_cart()
    b
start()