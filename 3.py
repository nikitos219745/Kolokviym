
#Чекалін Нікіта Валерійович 1 курс Завдання 3

#Створіть масив з пяти прізвищ і виведіть їх на екран стовпчиком,
#починаючи з останнього.


import numpy as np
while True:
    a = np.zeros(5, dtype=object)
    for i in range(5):
        a[i] = input("Введіть фамілію: ")#створення масиву і запис в нього значень
    print("Початковий список: ", a)
    for i in range(4,-1,-1):#виведення елементів навпаки
        print(a[i])

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break