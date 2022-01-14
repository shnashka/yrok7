# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
import random as r

x = 1200
y = 600
sd.resolution = (x, y)


class Snowflake:
    def __init__(self):
        self.x = r.randint(0, 1200)
        self.y = r.randint(550, 600)
        self.sped = r.randint(20, 100)
        self.length = r.randint(10, 60)
        self.point = sd.get_point(self.x, self.y)

    def edge(self):
        if self.y <= 0:
            return True

    def movement(self):
        self.point = sd.get_point(self.x, self.y)
        self.y -= self.sped
        sd.snowflake(center=self.point, length=self.length)
        self.x += r.randint(-10, 10)


def new_snowflake(N):
    flakes_snowflakes = []
    for i in range(N):
        flakes_snowflakes.append(Snowflake())
    return flakes_snowflakes


flakes = new_snowflake(100)

while True:
    sd.clear_screen()
    for flake in flakes:
        flake.movement()
    if flake.edge():
        flake.__init__()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
