# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

pas = "secret"

while True:
    att = input ("Введите пароль: ")
    if att == pas:
        print ("Пароль верный")
        break
    else:
        print ("Пароль некорректен, попробуйте снова!")
        continue
        