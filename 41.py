#Чекалін Нікіта Валерійович 1 курс Завдання 41
"""
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а."""

import numpy as np
while True:
    try:
        b = np.random.randint( -10, 10, size=10 )#створ послд за рах рандомц
        print("Масив: ", b)
        a = int(input("Введіть число а: "))
        count = 0
        i = 0
        m = b[i]
        while i < len(b):#задання  умови при якій буде викон подальше порівняння
            if b[i] > m:
                nm = i
                m = [nm]
            i += 1
        for i in range(len(b)):
            if b[i] == m:
                count+=1

        print("Максимальний елемент: ", m)
        if count == 1 and m <= a:  #умова на макс елемент
            flag = True
            print("Максимальний елемент унікальний та не перебільшує задане число",flag)
        else:
            print(False)

    except ValueError:
        print("Не коректне значення" )

    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
        break