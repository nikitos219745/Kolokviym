#Чекалін Нікіта Валерійович 1 курс Завдання 54

#Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
#однаковими значеннями.

import numpy as np
def bubblesort(list):#використовуємо сортування 
    n = len(list)
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            if list[j-1] > list[j]:
                list[j],list[j-1] = list[j-1], list[j]
    return list

while True:
    try:
        x = np.zeros(20, dtype=int)#створення масиву з нулями
        for i in range(len(x)):
            x[i] = int(input("Введіть значення елемементу: "))#введення елементів
        list = bubblesort(x)
        print(x)
        for i in range(len(x)):
            if list[i] == list[i+1]:#умова перевірки для наст елементу
                print("Повторюється елемент: ", list[i])
                break

    except ValueError:
        print("Не коректне значення")
    print('Бажаєте продовжити роботу?')
    ex = input("Якщо ні введіть 1, якщо так будь-який символ :")
    if ex == '1':
        print("Ви вийшли з програми")
        break
    else:
        continue
