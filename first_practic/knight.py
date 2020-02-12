# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

print("Стоит витязь на распутье, а перед ним камень с надписью:")
print("\n - Налево пойдёшь - коня потеряешь.\n - Направо пойдёшь - женишься.\n – А прямо пойдёшь – сам пропадешь!")
answer = input("Введите left (l), right (r) или forward (f): ").lower()
if answer == "left" or answer == "l": # любое условие
	print("Конь вам больше не доверяет")
elif answer == "right" or answer == "r":
	print("Вы чувствуете как кольцо всевластия медленно овладевает Вами…")
elif answer == "forward" or answer == "f":
	print("Вы видите как кто-то катается по ромашковому полю на велосипеде.")