#Чекалін Нікіта Валерійович 1 курс Завдання 54
"""
    В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
"""

import numpy as np

while True:
    try:
        n = int(input("Введіть кількість елементів: "))#введення к-ль елементів
        x = np.zeros(n, dtype=int)
        i = 0
        while i < len(x):             #визначенння довжини масиву
            b = int(input("Введіть 0 або 1 або 5: "))
            if x[i] == 0 or x[i] == 1 or x[i] == 5: #умова яку потребеють у задачі
                x[i] = b
                i += 1
            else:
                i -= 1

    except ValueError:
        print("Не коректне значення")
    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue