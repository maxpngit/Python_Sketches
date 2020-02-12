# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import turtle as t
import random as r

maxX = 0
maxY = 0

fig = {
        '30': ['purple', 'red', 'magenta', 'blue', 'cyan', 'orange'],
        '59': ['red', 'purple', 'blue', 'green', 'yellow', 'orange'],
        '60': ['magenta', 'purple', 'cyan', 'green', 'yellow', 'orange'] 
        }
case = ['30', '59', '60']

num = input ('Введите номер фигуры от 0 до 60: (Пример: 30, 45 или 60): ')

if not num:
        num = '29'

if int(num) < 30:
        temp2 = r.randint(30, 60)
        num = str(temp2)

screen = t.Screen()
screen.setup(800, 800)
t.shape("turtle")
t.bgcolor('black')
t.speed(25)
angle = int(num)

if not num in fig:
        temp = r.randint(0,2)
        num = case[temp]
        
for x in range(182):
	t.pencolor(fig[num][x%6])
	t.width(x/100+1)
	t.forward(x)
	t.left(angle)
	maxX = t.xcor()
	maxY = t.ycor()


t.penup()
t.goto (-350, 350)
t.pendown()
#t.pencolor(fig['30'][r.randint(0,5)])
t.pencolor('white')
t.hideturtle()
t.write('Угол поворота: ' + num)
t.penup()
t.goto (t.xcor() + 50, t.ycor() + 30)
t.showturtle()
t.mainloop()
