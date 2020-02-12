# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

week_day = input ("Введите число от 1 до 7: ")

if not week_day.isdigit():
    print("Необходимо ввести число от 1 до 7. Попробуйте снова!")
elif int (week_day)  == 1:
    print("Сегодня понедельник")
elif int (week_day)  == 2:
    print("Сегодня вторник")
elif int (week_day)  == 3:
    print("Сегодня среда")
elif int (week_day)  == 4:
    print("Сегодня четверг")
elif int (week_day)  == 5:
    print("Сегодня пятница")
elif int (week_day)  == 6:
    print("Сегодня суббота")
elif int (week_day)  == 7:
    print("Сегодня воскресенье")
else:
    print("Необходимо ввести число от 1 до 7. Попробуйте снова!")