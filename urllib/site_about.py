# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

from urllib.request import urlopen         # из модуля urllib импортируем функцию urlopen

main_url = 'https://yandex.ru'

# по заголовку title узнаем о чем сайт
open_url = main_url
u = urlopen(open_url)						# открываем URL на чтение
for line in u:								# читаем u по строкам
    line = line.decode("utf-8")				# преобразуем байт-строку в строку
    line = line.strip(" \n")				# отбрасываем начальные и конечные пробелы
    if '<title>' in line:					# находим tag <title>
        x = line.split('<title>')			# определяем его содержимое
        y = x[1].split('</title>')			# между <title> и </title>)
        print(open_url,'#',y[0].lower())	# и выводим его
		break								# информация получена, цикл считывания можно прервать