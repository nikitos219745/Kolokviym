#Чекалін Нікіта Валерійович 1 курс Завдання 45

"""
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
"""


import numpy as np
import math
from math import sqrt

while True:
    try:
       r = int(input("Введіть радіус півкруга криші  "))#запис радыусу
       my = []#створ масиву
       dx = r // 5
       x = 0
       while x < 2 * r - dx:#задання умови при якій будуть проводитись подальші обрахунки
           x += dx
           h = sqrt(x * (2 * r - x))
           my.append(round( h, 2))
       arr = np.array(my, dtype=int )
       print (arr)

    except ValueError:
        print("Не коректне значення")
    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
        break
