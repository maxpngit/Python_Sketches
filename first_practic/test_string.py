# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""


S = 'Текст'
print(S[0])
print('Срез строки: ', S[1:3])
print(len(S))
S1 = S.lower()
print(S1)
if(S.isalpha()):
    print('Строка соcтоит только из букв')