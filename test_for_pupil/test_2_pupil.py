# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import turtle as t

count = 0

t.shape("turtle")

t.pencolor('red')
t.fillcolor('yellow')
t.bgcolor("blue")

t.penup()
t.goto(-75, 75)
t.pendown()

t.begin_fill()

while count < 4:
    t.forward(150)
    t.right(90)
    count+=1

t.end_fill()
    
t.mainloop()

