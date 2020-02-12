# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

string = input("Введите любую строку: ")

strlen = len(string)
count = string.count('а')

if count:
    print("Буква 'а' есть в введенной строке и встречается " + str(count) + " раз(а).")
else:
    print("Буква 'а' в введенной строке не встречается.")
print("Длина введенной Вами строки - " + str(strlen) + ".")
