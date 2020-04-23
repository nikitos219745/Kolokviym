#Чекалін Нікіта Валерійович 1 курс Завдання 56

#Якщо в одновимірному масиві є три поспіль однакових елемента, то
#змінній r привласнити значення істина.
import numpy as np
while True:
    try:
        r = False
        n = int(input("Введіть кількість елементів: "))  #задання к-ль елементів 
        x = np.zeros(n, dtype=int)
        for i in range(n):
            x[i] = int(input())    #задання к-ль елементів через цикл
        print(x)
        for i in range(n):
            if x[i] == x[i+1] and x[i+1] == x[i+2]:     #задання умови перевірки на повтор ел
                r = True
                print("Повторюваний елемент", x[i], r)
                break
            else:
                print(r)
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
    
