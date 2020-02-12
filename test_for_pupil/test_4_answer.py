# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

voc = {
        'столица': 'capital',
        'страна': 'country',
        'город': 'town',
        'улица': 'street',
        'индекс': 'ZIP-code',
        'строение': 'building',
        'квартира': 'appartment'
        }

while True: # что это за цикл? При каких условиях он завершится?
        temp = input ('Введите слово для перевода (на русском): ')
        word = temp.strip()  # убираем пробелы в начале и в конце введенного слова
        word = word.lower() # делаем все буквы слова строчными

        if word # дописать условие проверки нахождения слова в словаре, поставив ':' в конце
                translate = voc[word]
                print (word, '-', translate)
                break 
        else:
                print ('Значение слова', word, 'отсутствует в словаре')
                continue






