# 26. Самый дешевый путь
# Ограничение времени	1 секунда
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# В каждой клетке прямоугольной таблицы
# N
# ×
# M
#  записано некоторое число. Изначально игрок находится в левой верхней клетке. За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).
# Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.
#
# Формат ввода
# Вводятся два числа N и M — размеры таблицы (
# 1
# ≤
# N
# ≤
# 2
# 0
# ,
# 1
# ≤
# M
# ≤
# 2
# 0
# ). Затем идет N строк по M чисел в каждой — размеры штрафов в килограммах за прохождение через соответствующие клетки (числа от 0 до 100).
# Формат вывода
# Выведите минимальный вес еды в килограммах, отдав которую можно попасть в правый нижний угол.
# Пример
# Ввод	Вывод
# 5 5
# 1 1 1 1 1
# 3 100 100 100 100
# 1 1 1 1 1
# 2 2 2 2 1
# 1 1 1 1 1
# 11
from typing import List, Tuple
import sys


def best_way(mapp: List[Tuple[int]], h: int, w: int) -> int:
    dp = [[0] * w for _ in range(h)]
    # fill first row and first column
    dp[0][0] = mapp[0][0]
    for i in range(1, h):
        dp[i][0] = dp[i - 1][0] + mapp[i][0]
    for j in range(1, w):
        dp[0][j] = dp[0][j - 1] + mapp[0][j]
    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + mapp[i][j]
    return str(dp[h-1][w-1])


if __name__ == '__main__':
    h, w = tuple(map(int, sys.stdin.readline().split()))
    matrix = []
    for _ in range(h):
        line = tuple(map(int, sys.stdin.readline().split()))
        matrix.append(line)
    print(best_way(matrix, h, w))