# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

string = input("Введите любую строку: ")

curpos = 0 # текущая буква в слове
count = 0 # сколько раз встречается буква
num = 0   # текущий номер(а) позиции буквы в слове
pos = " "  # итоговая строка, содержащая номера позиций в строке
strlen = 0 # длина строки

strlen = len(string)

while curpos < strlen:
    if string[curpos] == 'а':
        count += 1
        pos = pos + str(num + 1) + ", "
    num += 1
    curpos +=1
    pos.strip(",")
if count:
    print("Буква 'а' есть в введенной строке и встречается " + str(count) + " раз(а). Ее позиции: " + pos)
else:
    print("Буква 'а' в введенной строке не встречается.")
print("Длина введенной Вами строки - " + str(strlen) + ".")
