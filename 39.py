#Чекалін Нікіта Валерійович 1 курс Завдання 39
"""
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
"""
import numpy as np
while True:
    try:
        a = np.random.randint(-25,30, size=10)#створення рандомних значень для температури
        b = np.random.randint(1, 100, size=10)#створення рандомних значень для опадів
        count1 = 0
        count2 = 0
        for i in range(len(a)):#задання умови для перевірки к-ль утворення осадків при певній темпр
            if a[i] > 0:
                count2 += b[i]
            else:
                count1 += b[i]
        print("Данні про температуру: ",a)
        print("Данні про кількість опедів: ", b)
        print("Кількість опадів у вигляді снігу:  ",count1,"Кількість опадів у вигляді дощу:  ",count2)
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
