#Чекалін Нікіта Валерійович 1 курс Завдання 27

#Лінійний масив містить відомості про кількість опадів, що випали за
#кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
#опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
#місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.

import numpy as np

while True:
    try:

        t = np.zeros(12, dtype=int)
        for i in range(len(t)):#створення циклу 
            t[i] = int(input("Введіть кількість опадів: "))#вводимо значен яза доп циклу
            if 0 < t[i] < 2000:
                continue
            else:
                i -= 1
        i = 0
        k = 0
        s =0
        while i < len(t):
            if t[i] < 30:#перевірка на мін к-ль опадів
                k += t[i]
            s += t[i]
            i += 1
        print("Масив: ",t)
        print("Кількість посушливих днів: ",k,"Середня кількість опадів: ",s/12)
    except ValueError:
        print("Не коректне значення")

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
