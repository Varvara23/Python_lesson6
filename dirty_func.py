import random

# Функция из урока №4
def f(_list_word, _n):
    list_ret = []
    for i in range(_n):
        list_ret.append(random.choice(_list_word))
    return list_ret


# №2 Функция возвращает случайное число от 1 до х
def f_two(x):
    n = random.randint(0,x)
    return n
