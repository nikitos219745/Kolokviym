#Чекалін Нікіта Валерійович 1 курс Завдання 36

"""
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
"""

import numpy as np
while True:
    try:
        a = np.zeros(10, dtype=int)
        s = 0
        for i in range(len(a)):
            a[i] = int(input("Введіть число: "))#заповнення масиву елементами 
            if a[i] > 0:
                s += a[i]#задання умови для додавання
        print("Сумма: ", s)
        print("Масив: ", a)
    except ValueError:
        print ( "Не коректне значення" )

    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
        break
