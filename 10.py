#Чекалін Нікіта Валерійович 1 курс Завдання 10

#Дані про температуру повітря за декаду листопада зберігаються в масиві.
#Визначити, скільки разів температура опускалася нижче -10 градусів.



import numpy as np
while True:
    a = np.zeros(10, dtype=int)
    count = 0#лічильник
    for i in range(len(a)):
        a[i] = int(input("Введіть температуру:   "))#введення данних
    for i in range(len(a)):#умова для визнач к-ль опусканння темп
        if a[i] <= -10:
            count += 1#лічильник
    print("Масив ",a)
    print("Кількість раз, коли  температура була ниже -10: ",count)
    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break