# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

#Есть список из нескольких значений
lst = ['12', '15', '20', '25']

#Просим пользователя ввести число
num = input ('Введите число: ')

#используя if проверить есть ли число в списке

if num #---завершите написание условия
        print('Число ' + num + ' есть в списке')
    else:
        print('Числа ' + num + ' нет в списке')

#если пользователь ввел не число
 if not num.isdigit():
        print('"' + num + '" - это вовсе не число')
 