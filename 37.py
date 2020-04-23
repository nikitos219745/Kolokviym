#Чекалін Нікіта Валерійович 1 курс Завдання 37
"""
Розсортуйте заданий лінійний масив по зростанню.
"""
import numpy as np
while True:
    try:
        a = np.zeros(10, dtype=int)
        for i in range(len(a)):
            a[i] = int(input("Введіть число: "))#введення елементів в масив
        print("Масив: ", a)
        def BubbleSort(A):#застосуваня методу  бульбашковго сортування для сорт елементыв по зрост
            n = len(A)
            for i in range(1, n):
                for j in range(n - 1, i - 1, -1):
                    if A[j - 1] > A[j]:
                        A[j], A[j - 1] = A[j - 1], A[j]
            return A

        b = BubbleSort(a)
        print("Відсортований масив: ", b)
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
