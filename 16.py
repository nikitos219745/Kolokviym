#Чекалін Нікіта Валерійович 1 курс Завдання 16


#Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
#масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
import numpy as np
import random
while True:
    a = np.array([random.randint(10,50) for i in range(15)])#створення масиву і заповнення за доп рандому
    pr = 1
    for i in range(len(a)):
        if a[i] % 7 == 0:#визначення простого числа
            pr = pr*a[i]
        i += 1#лычильник
    print("Добуток: ",pr)
    print("Масив: ",a)
    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
