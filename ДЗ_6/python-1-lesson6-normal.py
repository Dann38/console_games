# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
"""
Я не помню когда мы писали игру, но я придумал свою, надеюсь задание выполнино верно
"""
import random
import re

class Turtel:
    def __init__(self):
        self.hp = 1000
        self.attack_arm_hp = 50

    def attack(self, attack_, player, fr):
        """
        :param attack_: сколько hp отнимается
        :param player: кого атакует
        :param fr: везение, число 1-10
        :return: отнимает hp при атаки
        """
        fortun = int(random.randint(0, 100))
        if fortun >100-100/fr:
            player.hp -= attack_
            print(f"-{attack_}hp")
        elif fortun >100/fr:
            player.hp -= attack_/2
            print(f"-{attack_/2}hp")
        else:
            print("промах")

class Leonarda(Turtel):
    def __init__(self):
        Turtel.__init__(self)
        self.name = "Лео"
        self.attacks = "1. удар рукой(урон 50hp, везенье 7)\n" \
                       "2. удар мечем(урон 100hp везенье 5)\n" \
                       "3. удар двумя мечами(урон 200hp везенье 2)"

    def attack1(self, player):
        Turtel.attack(self, self.attack_arm_hp, player, 7)

    def attack2(self, player):
        Turtel.attack(self, 100, player, 5)

    def attack3(self, player):
        Turtel.attack(self, 200, player, 2)

class Donatella(Turtel):
    def __init__(self):
        Turtel.__init__(self)
        self.name = "Дони"
        self.attacks = "1. удар рукой(урон 50hp, везенье 7)\n" \
                       "2. врашение шестом(урон 80hp везенье) 6\n" \
                       "3. удар шестом(урон 300hp везенье 1)"

    def attack1(self, player):
        Turtel.attack(self, self.attack_arm_hp, player, 7)

    def attack2(self, player):
        Turtel.attack(self, 80, player, 6)

    def attack3(self, player):
        Turtel.attack(self, 300, player, 1)

class Micilangelo(Turtel):
    def __init__(self):
        Turtel.__init__(self)
        self.name = "Мики"
        self.attacks = "1. удар рукой(урон 50hp, везенье 7)\n" \
                       "2. вращение нунчаками(урон 120hp везенье 4)\n" \
                       "3. удар нунчаками(урон 200hp везенье 2)"

    def attack1(self, player):
        Turtel.attack(self, self.attack_arm_hp, player, 7)

    def attack2(self, player):
        Turtel.attack(self, 120, player, 4)

    def attack3(self, player):
        Turtel.attack(self, 200, player, 2)

class Rafaaly(Turtel):
    def __init__(self):
        Turtel.__init__(self)
        self.name = "Лео"
        self.attacks = "1. удар рукой(урон 50hp, везенье 7)\n" \
                       "2. удар саей(урон 150hp везенье 3)\n" \
                       "3. бросок саи(урон 300hp везенье 1)"

    def attack1(self, player):
        Turtel.attack(self, self.attack_arm_hp, player, 7)

    def attack2(self, player):
        Turtel.attack(self, 150, player, 3)

    def attack3(self, player):
        Turtel.attack(self, 300, player, 1)

def attacks_(player, values):
    while True:
        print(player.attacks)
        i = input(":")
        if re.match("^[1-3]{1}$", i) != None:
            if i == "1":
                player.attack1(values)
                break
            elif i == "2":
                player.attack2(values)
                break
            elif i == "3":
                player.attack3(values)
                break
        print("неверный ввод")

def character(int_):
    if int_ == 1:
        return Leonarda()
    elif int_ == 2:
        return Donatella()
    elif int_ == 3:
        return Micilangelo()
    elif int_ == 4:
        return Rafaaly()



def start():
    print(" +++++++++++++++++++++++++++\n"
          "+ИГРА: БОЙ ЧЕРЕПАШЕК НИНДЗЯ +\n"
          " +++++++++++++++++++++++++++\n")
    while True:
        player1_answer = input("1-й игрок ВЫБИРИТЕ ПЕРСОНАЖА:\n\n"
                        "1. Леонарда\n"
                        "2. Донотелла\n"
                        "3. Микилянджело\n"
                        "4. Рафаэль\n:"
                        )

        if re.match('^[1-4]{1}$', player1_answer) != None:
            player1_answer = int(player1_answer)
            break
        print("неверный ввод")

    while True:
        player2_answer = input("2-й игрок ВЫБИРИТЕ ПЕРСОНАЖА:\n\n"
                            "1. Леонарда\n"
                            "2. Донотелла\n"
                            "3. Микилянджело\n"
                            "4. Рафаэль\n:"
                            )

        if re.match('^[1-4]{1}$', player2_answer) != None:
            player2_answer = int(player2_answer)
            break
        print("неверный ввод")

    player2 = character(player2_answer)
    player1 = character(player1_answer)

    move = 2
    while True:
        print(f"============================================\n"
              f"{player1.name} * {player1.hp}hp |  {player2.hp}hp * {player2.name}\n"
              f"============================================")
        if player1.hp <= 0:
            print("выйграл второй игрок")
            return
        elif player2.hp <= 0:
            print("выйграл первый игрок")
            return

        else:
            if move == 2:
                move = 1
                attacks_(player1, player2)
            elif move == 1:
                move = 2
                attacks_(player2, player1)



start()

while True:
    answer = input("Хотите сыграть ещё раз?")
    if answer == "Да" or "Yes" or "Y" or "yes" or "Д" or "да":
        start()
    elif answer == "Нет" or "нет" or "No" or "no" or "N" or "n" or "Н" or "н":
        break
    else:
        print("не коректный ответ")
