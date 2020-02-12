# -*- coding: utf-8 -*-
"""
@author: Andrew Roboschool
"""

set = {'один','два','три'}
set2 = {'три', 'четыре'}

set.remove('один')
set.add('пять')
set.update(['семь', 'четыре'])

for item in set:
    print(item)

if "пять" in set:
    print("Да! Элемент есть в множестве!!!")

print("Размер множества: ", len(set), " значений!")


print("Пересечение: ", set.intersection(set2))
print("Разница: ", set.difference(set2))
print("Симметрическая разница: ", set.symmetric_difference(set2))
