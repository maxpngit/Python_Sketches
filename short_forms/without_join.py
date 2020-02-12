# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

names = ["Петя", "Митя", "Сеня", "Витя"]
#print(', '.join(str(x) for x in names))

print(*names, sep=', ')
