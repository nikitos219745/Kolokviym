
#Чекалін Нікіта Валерійович 1 курс Завдання 22

#Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
#Заповнення масиву здійснити випадковими числами від 5 до 500.

import numpy as np
import random
while True:
    try:
        a = np.array([random.randint(5,5000) for i in range(10)])#створення масиву і запис в нього значень
        s = 1
        for i in range(len(a)):
            if a[i] % 3 ==0 and a[i] % 9 == 0:#задання умови на кратність 3 і 9
                s = s * a[i]
        print("Масив: ",a)
        print("Добуток: ",s)
    except ValueError:
        print("Не коректне значення")

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
