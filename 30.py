#Чекалін Нікіта Валерійович 1 курс Завдання 30
"""
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
"""

import numpy as np
import random
while True:
    a = np.array([random.randint(10,100) for i in range(20)])#створення масиву за доп рандома
    print("Масив: ", a)
    i = 0
    m = a[i]
    mi = i
    while i < len(a):
        if a[i] < m:
            nm = i
            m = a[nm]
            mi = nm
        i += 1
    print(m,mi)
    b = a[mi+1::]
    s = 0
    for i in range(len(b)):
        s +=b[i]
    print(b)
    print("Середнє арифметичне за мінімальним : ",s/len(b))
    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
