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

    def attack_arm(self, attack_, player):
        fortun = int(random.randint(0,100))
        if fortun >67:
            player.hp -= attack_


class Leonarda(Turtel):
    def __init__(self):
        Turtel.__init__(self)

# class Donatella(Turtel):
# class Micilangelo(Turtel):
# class Rafaaly(Turtel):

player1 = Leonarda()
player2 = Leonarda()

print(player1.hp)
print(player2.hp)

player1.attack_arm(player1.attack_arm_hp, player2)

print(player1.hp)
print(player2.hp)