# coding=utf-8

"""

Функция, основанная на нахождении остатка от деления на 2

+ Максимально простая и понятная функция

- Работает медленнее с большими числами
- Не подходит для дробных чисел

"""


def isEven(value):
    return value % 2 == 0


"""

Функция, основанная на битовой операции И (AND)

Например, 5 в бинарной системе – 101
Выполнение операции И с 1 (001)
101 И 001  = 001 (1) - число нечётное

4 в бинарной системе –  100
Выполнение операции И с 1 (001)
100 И 001  = 000 (0) - число чётное

+ Очень эффективно работает с целыми числами любых размеров

- Не подходит для дробных чисел

"""


def myEven(value):
    return value & 1 == 0
