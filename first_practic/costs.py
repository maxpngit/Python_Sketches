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

    ###############################################    
    ###    index1 = sausage.find(".")           ###
    ###    index2 = sausage.find(",")           ###
    ###    if index1 > 0:                       ###
    ###        sausage = sausage[0:index1]      ###
    ###    elif index2 > 0:                     ###
    ###        sausage = sausage[0:index2]      ###
    ###############################################
      
    if (sausage.isdigit() and salad.isdigit() and bun.isdigit() and tea.isdigit()):
        break
    elif not sausage.isdigit():
        print ("Стоимость сосиски: " + sausage + " руб.? Нужно ввести число без копеек. Начнем сначала...\n")
        continue
    elif not salad.isdigit():
        print ("Стоимость салата: " + salad +  " руб.? Нужно ввести число без копеек. Начнем сначала...\n")
        continue   
    elif not bun.isdigit():
        print ("Стоимость булки: " + bun +  " руб.? Нужно ввести число без копеек. Начнем сначала...\n")
        continue
    elif not tea.isdigit():
        print ("Стоимость чая: " + tea +  " руб.? Нужно ввести число без копеек. Начнем сначала...\n")
        continue  
    else: 
        print ("Стоимость необходимо вводить цифрами. Начнем сначала...\n")
        continue
# тело цикла (завершение)       
# Если записать:
# ---        
#       total = sausage + salad + bun + tea
# ---        
# то вместо суммирования произойдет конкатенация строк, 
# результатом которой будет набор цифр, введенных пользователем         
    

total = int(sausage) + int(salad) + int(bun) + int(tea) 
print ("\nСуммарный расход составил: ", total, " рублей.")