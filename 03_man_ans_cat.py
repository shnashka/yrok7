# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):

        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 1500
        self.fullness -= 10

    def play(self):
        cprint('{} катка в дотан и заглотус на ротан '.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 100:
            cprint('{} сходил в магазин за едой'.format(self.name), color='green')
            cprint('{} сходил в магазин за едой пушку'.format(self.name), color='green')
            self.house.money -= 100
            self.house.food += 500
            self.house.cat_food += 500
        else:
            cprint('{} бомжара!'.format(self.name), color='red')

    def go_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} дом'.format(self.name), color='green')

    def do_cleaning(self):
        if self.house.mess <= 50:
            cprint('{} убрал дома'.format(self.name), color='green')
            self.fullness -= 10
        else:
            cprint('{} вызвал клининг'.format(self.name), color='yellow')
            self.house.money -= 50

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 1000:
            self.work()
        elif self.house.cat_food <= 10:
            self.shopping()
        elif self.house.mess > 50:
            self.do_cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.do_cleaning()
        else:
            self.play()


class House:

    def __init__(self):
        self.food = 50
        self.money = 1000
        self.cat_food = 10
        self.mess = 10

    def __str__(self):
        return 'В доме еды осталось {},еды для кота {}, денег  {}, уют {}'.format(
            self.food, self.cat_food, self.money, self.mess)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я кот - {}, сытость - {}'.format(self.name, self.fullness)

    def houmi(self, house):
        self.house = house
        cprint('Кот {} есть дом'.format(self.name), color='yellow')

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот {} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.cat_food -= 10
        else:
            cprint('у пушистого {} нет еды'.format(self.name), color='red')

    def ran(self):
        cprint('Кот {} бегает как ебантый '.format(self.name), color='yellow')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('Котик {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        else:
            self.ran()


house = House()
hom = Man(name='генадий')
cat = Cat(name='рюк')
hom.go_house(house)
cat.houmi(house)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    hom.act()
    cat.act()
    print('--- в конце дня ---')
    print(hom)
    print('-------------------------------------------')
    print(cat)
    print('-------------------------------------------')
    print(house)
