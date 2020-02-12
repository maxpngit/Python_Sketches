# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import turtle as t

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t.bgcolor('black')
t.speed(25)
angle = 59 # Рисует разноцветные спирали. Меняя значения, получаем различные фигуры

for x in range(182):
	t.pencolor(colors[x%6])
	t.width(x/100+1)
	t.forward(x)
	t.left(angle)

t.mainloop()