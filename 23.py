#Чекалін Нікіта Валерійович 1 курс Завдання 23

#Знайти суму всіх елементів масиву цілих чисел, які менше середнього
#арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
#здійснити випадковими числами від 150 до 300.


import numpy as np
import random
while True:
    try:
        a = np.array([random.randint(150,300) for i in range(20)])#створення масиву і запис в нього значень
        s = 0
        for i in range(len(a)):
            if a[i] < np.average(a):#метод для знах серед знач і орівняння
                s += a[i]
        print("Масив: ",a)
        print("Сумма: ",s)
    except ValueError:
        print("Не коректне значення")

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break