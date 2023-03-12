# 22. Кузнечик
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# У одного из студентов в комнате живёт кузнечик, который очень любит прыгать по клетчатой одномерной доске. Длина доски — N клеток. К его сожалению, он умеет прыгать только на 1, 2, …, k клеток вперёд.
#
# Однажды студентам стало интересно, сколькими способами кузнечик может допрыгать из первой клетки до последней. Помогите им ответить на этот вопрос.
#
# Формат ввода
# В первой и единственной строке входного файла записано два целых числа — N и k .
#
# Формат вывода
# Выведите одно число — количество способов, которыми кузнечик может допрыгать из первой клетки до последней.
#
# Пример
# Ввод	Вывод
# 8 2
# 21
from typing import List
import sys

def juping(n: int, k: int)->int:
    dp = [0] *(n + 1)
    dp[0] = 1
    # k = n if k > n else k
    for i in range(1, n + 1):
        r = k
        if (i < r):
            r = i
        for j in range(1, r + 1):
            dp[i] = dp[i] + dp[i - j]
    return str(dp[n])


def kuz(n, k):
    """
    определить сколькими способами кузнечик допрыгает до точки n,
    прыжками вплоть до k-шагов
    """
    a = []
    a.append(1)
    for i in range(1, n + 1):
        r = k
        if (i < r):
            r = i
        a.append(0)
        for j in range(1, r + 1):
            a[i] = a[i] + a[i - j]
    return str(a[n])

# if __name__=='__main__':
#     n, k = tuple(map(int, sys.stdin.readline().split()))
#     n, k = 10, 10
    # assert juping(n, k) == 89
    # sys.stdout.write(juping(n,k) + '\n')
    # print(kuz(n,k))
    # assert juping(1, 1) == 1
    # assert juping(2, 1) == 1
    # assert juping(3, 2) == 2
    # assert juping(10, 3) == 274
    # assert juping(15, 4) == 2105
    # assert juping(20, 5) == 4736


import sys
n, k = tuple(map(int, sys.stdin.readline().split()))
dp = [0] *(n + 1)
dp[0] = 1
for i in range(1, n + 1):
    r = k
    if r > i:
        r = i
    for j in range(1, r + 1):
        dp[i] = dp[i] + dp[i - j]
sys.stdout.write(str(dp[n - 1]))



