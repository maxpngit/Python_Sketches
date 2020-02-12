# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

lst = ['12', '15', '20', '25']

num = input ('Введите число: ')

if num in lst:
    print('Число ' + num + ' есть в списке')
else:
    print('Числа ' + num + ' нет в списке')

if not num.isdigit():
        print('"' + num + '" - это вовсе не число')
