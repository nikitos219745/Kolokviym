#Чекалін Нікіта Валерійович 1 курс Завдання 32
"""
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
"""
import numpy as np

while True:
    try:
        t = False
        a = np.zeros(12, dtype=int)
        countv, countp = 0, 0
        for i in range(len(a)):
            a[i] = int(input("Введіть число: "))#заповнення масиву елементами
            if a[i] < 0:
                countv += 1
            if a[i] % 2 == 0:#умова для перевірки на від'ємне і парне число
                countp +=1
        print(a)
        if countp >= 1 and countv >= 1:
            t = True
            print("Умова виконується", t)
        else:
            print("Умова не виконується", t)

    except ValueError:
        print("Не коректне значення")

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
