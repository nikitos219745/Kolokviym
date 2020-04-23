#Чекалін Нікіта Валерійович 1 курс Завдання 58

#Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
#повторюється найчастіше число.

import numpy as np

while True:
    try:
        n = int(input("Введіть кількість чисел: ")) #створення масиву з нулями
        x = np.zeros(n, dtype=int)
        for i in range(n):
            x[i] = int(input("Введіть елемент : "))  #запис елементів
        unique, pos = np.unique(x, return_inverse=True )   
        count = np.bincount(pos)            #Цей метод використовуєv для підрахунку частоти кожного елемента в масиві 
        max = count.argmax()             #Повертаєм індекси max елемента 
        print("Найбільше повторюється:", unique[max],count[max], " -раз")

    except ValueError:
        print("Не коректне значення")
    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
    
