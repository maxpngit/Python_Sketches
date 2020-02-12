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

while True:
        temp = input ('Введите слово для перевода (на русском): ')
        word = temp.strip()
        word = word.lower()

        if word in voc:
                translate = voc[word]
                print (word, '-', translate)
                break
        else:
                print ('Значение слова', word, 'отсутствует в словаре')
                newkey = 'А как слово "' + word + '" переводится? Введите: '
                newword = input (newkey)
                newword = newword.strip()
                newword = newword.lower()
                voc[word] = newword
                print ('Перевод слова "', word, '" добавлено в словарь со значением "', newword, '"')
                continue