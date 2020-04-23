
#Чекалін Нікіта Валерійович 1 курс Завдання 30
#Знайти кількість парних елементів одновимірного масиву.

import numpy as np
import random
while True:
    a = np.array([random.randint(10,100) for i in range(20)])#створення масиву і запис в нього значень
    count = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:#задання умови на знах парних чисел
            count+=1
    print("Масив: ",a)
    print("Кількість парних чисел: ",count)
    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
