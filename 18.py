#Чекалін Нікіта Валерійович 1 курс Завдання 18

#Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
#масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.

import numpy as np

while True:
    try:
        a = np.array([int(input("Введіть число: ")) for i in range(10)])#створення і запов ел масиву
        p = 1
        for i in range(len(a)):
            if a[i] < 0:#умова на знах числа менше 0
                p = p * a[i]
        print("Масив: ",a)
        print("Добуток: ",p)
    except ValueError:
        print("Не коректне значення")

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break