#Чекалін Нікіта Валерійович 1 курс Завдання 43

"""
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
"""


import numpy as np
while True:
    try:
        mas = np.random.randint(-10, 10, size=10)#створення послдовнст за рах рандомізац
        print("Масив: ", mas)
        w = False
        a, b = int(input("Введіть число a  ")), int(input("Введіть число b  "))
        for i in range(len(mas)):
            if mas[i] % a == 0 and mas[i] % b != 0: #заданння умови кратності і некратності
                w = False
        print("Якщо в одномірному цілочисельному масиву є хоча б 1 елемент кратний a і не кратний b w = True в інщому "
              "випадку w = False")
        print('w = ', w)
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