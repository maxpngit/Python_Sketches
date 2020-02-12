# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
ОДНОСТРОЧНИКИ И ИХ ПРИМЕНЕНИЕ
"""

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
res = []

for item in num:
    if item % 2:
        res.append(item)
print (res)
"""

res = [item for item in num if item % 2]
print (res)





        

