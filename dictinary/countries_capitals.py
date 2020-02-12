# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

Capitals = dict()
Capitals['Russia'] = 'Moscow'
Capitals['Germany'] = 'Berlin'
Capitals['Canada'] = 'Ottawa'

Countries = ['Russia', 'Germany', 'Canada', 'USA']

for country in Countries:
	if country in Capitals:
        print('Столица страны ' + country + ': ' + Capitals[country] + ';')    
	else:
		print('Страна c названием ' + country + ' отсутствует в словаре.')
