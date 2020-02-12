# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import pickle

# загружаем словарь из файла
with open('dict.dat', 'rb') as dump_in:
    voc = pickle.load(dump_in)

while True:
        temp = input ('Введите слово для перевода (на русском) или "#" для завершения: ')
        word = temp.strip()
        word = word.lower()

        if word == '#':
                break;

        if word in voc:
                translate = voc[word]
                print (word, '-', translate)
                continue
        else:
                print ('Значение слова', word, 'отсутствует в словаре')
                newkey = 'А как слово "' + word + '" переводится? Введите: '
                newword = input (newkey)
                newword = newword.strip()
                newword = newword.lower()
                voc[word] = newword
                print ('Перевод слова "', word, '" добавлено в словарь со значением "', newword, '"')
                continue

# сохраняем словарь в файл
with open('dump.dat', 'wb') as dump_out:
    pickle.dump(voc, dump_out)

# загружаем словарь из файла
with open('dump.dat', 'rb') as dump_in:
    der = pickle.load(dump_in)

print("Теперь наш словарь содержит:\n")

for key, value in der.items():
    print(key, '-', value)
