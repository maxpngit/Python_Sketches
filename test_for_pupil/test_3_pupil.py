# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

string = input("Введите любую строку: ")

count = 0 # сколько раз встречается буква
num = 0   # текущий номер(а) позиции буквы в слове
pos = " " # итоговая строка, содержащая номера позиций в строке

for char in string:
    if char.lower() == 'а':
        count += 1
        pos = pos + str(num + 1) + ", "
    num += 1    
if count:
    print("Буква 'а' есть в введенной строке и встречается " + str(count) + " раз(а). Ее позиции: " + pos)
else:
    print("Буква 'а' в введенной строке не встречается.")
print("Длина введенной Вами строки -", len(string), ".")