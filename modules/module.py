# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import my_math as m
import hello as h

i = 0
j = 2
strn = ''

print(h.test())

my_list = ['нулевой', 'первый', 'второй', 'третий', 'четвертый', 'пятый', 'шестой', 'седьмой', 'восьмой', 'девятый']

while (i <= 20):
    strn = 'Элемент: ' + '"' + my_list[m.mod(i,j)] + '", как остаток от деления ' + str(i) + ' на ' + str(j)
    print(strn)
    i += 1
