#Чекалін Нікіта Валерійович 1 курс Завдання 54
"""
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
"""
import numpy as np
from random import sample
while True:
    try:

        a = np.array(sample(range(1, 100), 10))   #створення послідовності через цикл в яких  10 вигр білетів
        n = int(input("Введіть номер виграшного білету: "))
        с = 0
        for i in range(len(a)):
            if a[i] == n:#перевірка на виграшність білету
                с += 1
        if с == 1:
            print("Білет виграшний")
        else:
            print("Білет не виграшний")

        print("Виграшні білети :",a)

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
