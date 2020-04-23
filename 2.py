#Чекалін Нікіта Валерійович     1 курс  Колоквіум   Завдання 2

"""
Введіть з клавіатури в масив  X  5 цілочисельних елементів.
Виведіть на екран значення їх коренів та квадратів
"""
import math
import numpy as np
while True:
    try:
        x = np.array([int(input("Введіть число: ")) for i in range(5)])#створення масиву і запис в нього значень
        k = np.zeros((2,5),dtype=float)
        for i in range(2):
            for j in range(len(x)):
                k[0][j] = x[j]**2#обрахунок (квадрат)
                k[1][j] = math.sqrt(x[j])#обрахунок,корінь
        print("Масив: ", x)
        print("Значення коренів та квадратів елементів масиву: ",k)
    except ValueError:
        print("Не коректне значення")
    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
