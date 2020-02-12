# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

#Программа "Перечень расходов"
# ---
#Изучаем:
#1. булевую логику и цикл while
#2. break и continue
#3. Преобразование строки в целое число
#4. Проверку на ввод числа
# ---
#Закрепляем:
#1. input и print
#2. if, elif и else
#3. конкатенацию строк
#4. срезы строк


print ("Произведем подсчет расходов в буфете.")
print ("Ввводите стоимость без копеек:\n")

total = 0

while True:
# тело цикла (начало)
    sausage = input ("Сосиска в тесте: ")
    salad = input ("Салат \"Цезарь\": ")
    bun = input ("Слоенная булка: ")
    tea = input ("Чай с сахаром: ")
    

        
    
# Проверяем ввод стоимости для сосиски:
    index1 = sausage.find(".")
    index2 = sausage.find(",") 
    if index1 > 0:                       
        sausage = sausage[0:index1]
        sausage = int(sausage)
    elif index2 > 0:
       sausage = sausage[0:index2]
       sausage = int(sausage)
    elif not sausage.isdigit():   
        sausage = '0'
        sausage = int(sausage)
    else:
        sausage = int(sausage)
# завершение проверки стоимости сосиски
#--------------------------------------
# Проверяем ввод стоимости для салата:
    index1 = salad.find(".")
    index2 = salad.find(",")         
    if index1 > 0:                       
        salad = salad[0:index1]
        salad = int(salad)
    elif index2 > 0:
       salad = salad[0:index2]
       salad = int(salad)
    elif not salad.isdigit():   
       salad = '0'
       salad = int(salad)
    else:
       salad = int(salad)
# завершение проверки стоимости сосиски
#--------------------------------------
# Проверяем ввод стоимости для булки:
    index1 = bun.find(".")
    index2 = bun.find(",")                
    if index1 > 0:                       
        bun = bun[0:index1]
        bun = int(bun)
    elif index2 > 0:
       bun = bun[0:index2]
       bun = int(bun)
    elif not bun.isdigit():   
       bun = '0'
       bun = int(bun)
    else:
       bun = int(bun)
# завершение проверки стоимости булки
#--------------------------------------
# Проверяем ввод стоимости для чая:
    index1 = tea.find(".")
    index2 = tea.find(",")                
    if index1 > 0:                       
        tea = tea[0:index1]
        tea = int(tea)
    elif index2 > 0:
       tea = tea[0:index2]
       tea = int(tea)
    elif not tea.isdigit():   
       tea = '0'
       tea = int(tea)
    else:
        tea = int(tea)
# завершение проверки стоимости чая
#--------------------------------------
      
    if sausage and salad and bun and tea:
        break
    elif not sausage:
        print ("Стоимость сосиски: " + str(sausage) + " руб.? Не верю! Начнем сначала...\n")
        continue
    elif not salad:
        print ("Стоимость салата: " + str(salad) +  " руб.? Не верю! Начнем сначала...\n")
        continue   
    elif not bun:
        print ("Стоимость булки: " + str(bun) +  " руб.? Не верю! Начнем сначала...\n")
        continue
    elif not tea:
        print ("Стоимость чая: " + str(tea) +  " руб.? Не верю! Начнем сначала...\n")
        continue  
    else: 
        print ("Стоимость должна быть отлична от нуля. Начнем сначала...\n")
        continue
# тело цикла (завершение)       

total = sausage + salad + bun + tea 
print ("\nСуммарный расход составил: ", total, " рублей.")