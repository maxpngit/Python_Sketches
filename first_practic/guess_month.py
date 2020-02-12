# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

month_day = input ("Введите номер календарного месяца: от 1 до 12: ")

if not month_day.isdigit():
    print("Такого месяца в календаре нет! Введите число от 1 до 12!")
elif month_day == '1':
    print("На дворе ЯНВАРЬ: Новый ГОД!")
elif month_day == '2':
    print("На дворе ФЕВРАЛЬ: последний месяц зимы")
elif month_day == '3':
    print("На дворе МАРТ: Весна пришла!!!")
elif month_day == '4':
    print("На дворе АПРЕЛЬ: Звучит капель...")
elif month_day  == '5':
    print("На дворе МАЙ: Последний месяц и КАНИКУЛЫ!!!")
elif month_day  == '6':
    print("На дворе ИЮНЬ: УРА! ЛЕТО!!!")
elif month_day  == '7':
    print("На дворе ИЮЛЬ: Пора на море!!!")
elif month_day  == '8':
    print("На дворе АВГУСТ: Скоро в школу :)")
elif month_day  == '9':
    print("На дворе СЕНТЯБРЬ: УРА! Снова в школу!")
elif month_day  == '10':
    print("На дворе ОКТЯБРЬ: Поздравляем учителей!")
elif month_day  == '11':
    print("На дворе НОЯБРЬ: КАНИКУЛЫ!!!")
elif month_day  == '12':
    print("На дворе ДЕКАБРЬ: Cкоро Новый ГОД!")
else:
    print("Такого месяца в календаре нет! Введите число от 1 до 12!")