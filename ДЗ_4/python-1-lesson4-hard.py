# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!
import re
person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]

person = {}
card_number = 0
pin_code = 0
choice = 0
count = 0


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person_, money):
    global person

    if person_['money'] > money:
        person_['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def process_user_choice(choice, person):
    global count
    pattern_money = '[0-9]'
    if choice == 1:
        return check_account(person)
    elif choice == 2:

        while True:
            count = input('Сумма к снятию:')
            if (re.match(pattern_money, count)) == None:
                print("Не корректно введена сумма")
            else:
                count = float(count)
                break
        return withdraw_money(person, count)

def start():
    global person
    global card_number
    global pin_code
    global choice
    pattern = '^[0-9]{16}\s{1}[0-9]{4}$'
    pattern_choice = '[1-3]{1}'
    while True:
        info = input('Введите номер карты и пин код через пробел:')
        if (re.match(pattern, info)) == None:
            print("Не коректно введена информация")
        else:
            break
    card_number, pin_code =info.split()

    card_number = int(card_number)
    pin_code = int(pin_code)
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:')
            if (re.match(pattern_choice, str(choice))) == None:
                print("Не корректный запрос")
                continue
            else:
                choice = int(choice)
                if choice == 3:
                    break
                print(process_user_choice(choice, person))
    else:
        print('Номер карты или пин код введены не верно!')


start()
