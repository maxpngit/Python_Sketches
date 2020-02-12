# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import os

print("Имя нашей операционной системы:", os.name)
print("Список файлов в нашей папке: ", os.listdir())
print("Мы можем видеть среди этих файлов наш 'text.txt'.")
print("А теперь удалим: 'text.txt'.")
os.remove ("text.txt")
print("И посмотрим список снова:")
print(os.listdir())
