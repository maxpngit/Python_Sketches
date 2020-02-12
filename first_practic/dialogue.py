# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

text = "Привет"
name = input ('Введите имя: ')
print (text, name)
animal = input ('У тебя есть кошка (да/нет): ')
if (animal == 'нет'):
    print ("Ого,", name, ", у тебя нет кошки?")
else:
    print ("Ого,", name, ", здорово!")
    cat = input ('И как ее зовут?: ')
if (cat!= ''):
    print (text, name, "! Твою кошку зовут -", cat)
else:
    print (text, name, "! Как жаль, что у тебя нет кошки")
    