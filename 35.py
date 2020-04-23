#Чекалін Нікіта Валерійович 1 курс Завдання 35
"""Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
"""

import numpy as np
while True:
    try:
        a = np.zeros(6, dtype=int)
        for i in range(len(a)):
            a[i] = int(input("Введіть число: "))#заповнення масиву елементами 
        c = a.copy()
        def BubbleSort(A):
            n = len(A)
            for i in range(1, n):
                for j in range(n - 1, i - 1, -1):#застосуваня методу  бульбашковго сортування для сорт елементыв по спаданню
                    if A[j - 1] < A[j]:
                        A[j], A[j - 1] = A[j - 1], A[j]
            return A
        b = BubbleSort(c)
        if a == b:
            print("Елементи розміщені за спаданням")
        else:
            print("Елементи не  розміщені за спаданням")
    except ValueError:
        print ( "Не коректне значення" )

    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
        break
