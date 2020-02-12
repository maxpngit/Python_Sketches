# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

F = open("text.txt")
line1 = F.readline()
line2 = F.readline()
print("Имя файла: ", F.name)
print ("Из него прочитано: ")
print ("Строка №1:", line1)
print ("Строка №2:", line2) 
print("В каком режиме файл открыт: ", F.mode)
print("Файл закрыт? (True или False): ", F.closed)
F.close()
print("А теперь закрыт? (True или False): ", F.closed)
