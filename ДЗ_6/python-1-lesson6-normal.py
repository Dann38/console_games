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
    def arm(self, player):
        Turtel.attack(self, self.attack_arm_hp, player, 7)
    def sword(self, player):
        Turtel.attack(self, 100, player, 5)
    def sword2(self, player):
        Turtel.attack(self, 200, player, 2)





# class Donatella(Turtel):
# class Micilangelo(Turtel):

# class Rafaaly(Turtel):

player1 = Leonarda()
player2 = Leonarda()

print(player1.hp)
print(player2.hp)
print(player1.hp)
print(player2.hp)

def character(int_, player):
    if int_ = 1:
        player = Leonarda()
    elif int_ = 2:
        player = Donatella()
    elif int_ = 3:
        player = Micilangelo()
    elif int_ = 4:
        player = Rafaaly()



def start():
    print("ИГРА: БОЙ ЧЕРЕПАШЕК НИНДЗЯ")
    player1 = input("ВЫБИРИТЕ ПЕРСОНАЖА:\n"
                        "1. Леонарда\n"
                        "2. Донотелла\n"
                        "3. Микилянджело\n"
                        "4. Рафаэль\n"
                        )
    player1 = int(player1)
    character(player1, player1)


    player2 = input("ВЫБИРИТЕ ПЕРСОНАЖА:\n"
                        "1. Леонарда\n"
                        "2. Донотелла\n"
                        "3. Микилянджело\n"
                        "4. Рафаэль\n"
                        )
    player2 = int(player1)
    character(player1, player1)



start()