#Чекалін Нікіта Валерійович 1 курс Завдання 42
"""
Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
"""

import numpy as np
while True:

    a = np.random.randint( -10, 10, size=10 )#ствр послд за рах рандомізац
    print("Масив: ", a)
    count = 0
    for i in range(len(a)):#запис і визначеня  довжини елементів мас
        fact = 1
        b = 0
        while b < i:#задданя умови для не рівності i*i<ai<i
            b += 1
            fact = fact * b
        if i*i < a[i] < fact:
            count+=1
    print("Кількість елементів для яких виконується рівність i*i<a[i]<i! : ",count)

    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
        break
