# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
# print(
#     '1 Вода\n'
#     '2 Огонь\n'
#     '3 Земля\n'
#     '4 Воздух\n'
#     'введите две цыфры через пробел\n'
# )


class Water:
    def __str__(self):
        return 'вода'

    def __add__(self, other):
        if isinstance(other, Water):
            return Water()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Fire:
    def __str__(self):
        return 'огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Fire):
            return Fire()
        elif isinstance(other, Earth):
            return Lava()

        else:
            return None


class Earth:
    def __str__(self):
        return 'земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Earth):
            return Earth()
        else:
            return None


class Air:
    def __str__(self):
        return 'воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Air):
            return Air()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'

class perdezh:
    def __str__(self):
        return 'пердеж'

    def __add__(self, other):
        if isinstance(other, Water):
            return podliva()
        elif isinstance(other, Air):
            return holostoy()
        elif isinstance(other, Fire):
            return hachepuri()
        elif isinstance(other, Earth):
            return rip()
        else:
            return None


class Steam:
    def __str__(self):
        return 'Пар'
class podliva:
    def __str__(self):
        return 'с подливкой '
class hachepuri:
    def __str__(self):
        return 'горит очко '
class rip:
    def __str__(self):
        return 'я есть грут '
class holostoy:
    def __str__(self):
        return 'хлопок '


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())

print(perdezh(), '+', Air(), '=', perdezh() + Air())
print(perdezh(), '+', Fire(), '=', perdezh() + Fire())
print(perdezh(), '+', Water(), '=', perdezh() + Water())
print(perdezh(), '+', Earth(), '=', perdezh() + Earth())
