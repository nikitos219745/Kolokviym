#Чекалін Нікіта Валерійович 1 курс Завдання 38
"""
Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
"""


import numpy as np
while True:
    try:
        a = np.random.randint(1,25, size=(10,4))  #створення рандомних чисел
        print("Стовпчик:  1 - західний, 2 - східний, 3 - північний, 4 - південний")
        count = 0      #лічильник
        for i in range(10):
            if a[i][2] > 8:#задання умови на перевірку сили вітру
                count += 1
        print("Данні: ",a)
        print("Cкільки раз дув північний вітер з силою більшою ніж 8 м/с:  ",count)
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