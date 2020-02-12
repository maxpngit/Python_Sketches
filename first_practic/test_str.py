# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

S1 = 'арутюнов'
S2 = 'АДАМ' 
S3 =' '
print(S1 + S3 + S2) 
print('Алексей ' * 3)
print(S2[3])
print(S2[3:6])
S4 = len(S2)
print(S4) 
print(S1[0]) 
print('Срез строки S2: ', S2[1:3]) #Выведет ан
print(len(S2)) 
S5 = S2.lower() 
print(S5) 
print(S1.upper())
if(S2.isalpha()):
    print('Строка состоит только из букв')
else:
    print('Строка состоит не только из букв')
S6 = S1.lower()
if(S6=='арутюнов'):
    print('Это Манвел')
if(S1.istitle()):
    print('Фамилия начинается с заглавной буквы')
else:
    print('Фамилии не пишутся с маленькой буквы')
 