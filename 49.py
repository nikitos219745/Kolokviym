#Чекалін Нікіта Валерійович 1 курс Завдання 49

"""Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої UA гривень.
"""
import numpy as np
while True:
    try:
        n = int(input("Введіть кількість послуг: "))#запис к-ль послуг
        a = np.zeros(n,dtype=object)
        b = np.zeros(n,dtype=int)
        for i in range(n):
            a[i] = input("Введіть послугу: ")#запис послуг через цикл
            b[i] = int(input("Введіть ціну : "))#запис цін через цикл
        print(a)
        print(b)
        c,d = 0,0
        p = int(input("Введіть ціну ua : "))
        for i in range(n):
            if p == b[i]:
                c = a[i:]#задання умови
                d = b[i:]
        print(c)
        print(d)


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
