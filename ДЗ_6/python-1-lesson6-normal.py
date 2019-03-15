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
        fortun = int(random.randint(0,100))
        if fortun >100-100/fr:
            player.hp -= attack_
        elif fortun >100/fr:
            player.hp -= attack_/2
        else:
            pass



class Leonarda(Turtel):
    def __init__(self):
        Turtel.__init__(self)
        self.attacks = "1. удар рукой(урон 50hp, везенье 7\n" \
                       "2. удар мечем(урон 100hp везенье 5\n" \
                       "3. удар двумя мечами(урон 200hp везенье 2"
    def attack1(self, player):
        Turtel.attack(self, self.attack_arm_hp, player, 7)
    def attack2(self, player):
        Turtel.attack(self, 100, player, 5)
    def attack3(self, player):
        Turtel.attack(self, 200, player, 2)





# class Donatella(Turtel):
# class Micilangelo(Turtel):

# class Rafaaly(Turtel):

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
    print("ИГРА: БОЙ ЧЕРЕПАШЕК НИНДЗЯ")
    while True:
        player1_answer = input("ВЫБИРИТЕ ПЕРСОНАЖА:\n"
                        "1. Леонарда\n"
                        "2. Донотелла\n"
                        "3. Микилянджело\n"
                        "4. Рафаэль\n"
                        )
        if re.match('^[1-4]{1}&', player1_answer) != None:
            player1_answer = int(player1_answer)
            break

    while True:
        player2_answer = input("ВЫБИРИТЕ ПЕРСОНАЖА:\n"
                            "1. Леонарда\n"
                            "2. Донотелла\n"
                            "3. Микилянджело\n"
                            "4. Рафаэль\n"
                            )
        if re.match('^[1-4]{1}$', player2_answer) != None:
            player2_answer = int(player2_answer)
            break

    player2 = character(player2_answer)
    player1 = character(player1_answer)


start()