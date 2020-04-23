#Чекалін Нікіта Валерійович 1 курс Завдання 59

#Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
#чисел в ньому.


import numpy as np
while True:
    try:
        x = np.zeros(10, dtype=int)               #створення масиву з нулями
        for i in range(10):
            x[i] = int(input("Введіть елемент : "))      #запис елементів
        unique, pos = np.unique(x, return_inverse=True )       
        count = np.bincount(pos)
        max = count.argmax()                        #Повертаєv індекси max елемента 
        print("Найбільше повторюється:", unique[max],count[max], " рази")  
        print("Кількість чисел які не повторюються: ", 10 - count[max])
    except ValueError:
        print("Не коректне значення")
    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
