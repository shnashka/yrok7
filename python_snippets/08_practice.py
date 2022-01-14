# -*- coding: utf-8 -*-

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 1500
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} подрочил'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='green')
            self.house.money -= 50
            self.house.food += 500
        else:
            cprint('{} бомжара!'.format(self.name), color='red')

    def cat_shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой пушку'.format(self.name), color='green')
            self.house.money -= 50
            self.house.cat_food += 500

    def do_cleaning(self):
        if self.house.mess <= 50:
            cprint('{} убрал дома'.format(self.name), color='green')
            self.fullness -= 10
        else:
            cprint('{} вызвал клининг'.format(self.name), color='magenta')
            self.house.money -= 50

    def feed_cat(self):
        if self.house.cat_food >= 20:
            cprint('{} насыпал корма котику'.format(self.name), color='magenta')
            self.house.cat_food -= 20
            self.house.cat_plate += 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food <= 10:
            self.cat_shopping()
        elif self.house.mess > 50:
            self.do_cleaning()
        elif self.house.cat_plate <= 10:
            self.feed_cat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.do_cleaning()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.mess = 0
        self.cat_plate = 0

    def __str__(self):
        return 'В доме еды осталось {},еды для котика {},в миске {}, денег осталось {}, степень срача {}'.format(
            self.food, self.cat_food, self.cat_plate, self.money, self.mess)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я котик - {}, сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_plate >= 10:
            cprint('Котик {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_plate -= 10
        elif self.house.food >= 10:
            cprint('Котик {} спиздил колбасу!'.format(self.name), color='cyan')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('Котик {} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('Котик {} спал весь день '.format(self.name), color='yellow')
        self.fullness -= 10

    def tear_wallpaper(self):
        cprint('Котик {} подрал обои'.format(self.name), color='blue')
        self.house.mess += 10

    def find_house(self, house):
        self.house = house
        cprint('Котик {} нашел дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('Котик {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif 2 <= dice <= 3:
            self.tear_wallpaper()
        else:
            self.sleep()


house = House()
dude = Man(name='Чувак')
yakov = Cat(name='Яшка')
dude.go_to_the_house(house)
yakov.find_house(house)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    dude.act()
    yakov.act()
    print('--- в конце дня ---')
    print(dude)
    print('-------------------------------------------')
    print(yakov)
    print('-------------------------------------------')
    print(house)


class House:

    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
