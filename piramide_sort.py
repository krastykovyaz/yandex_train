# 20. Пирамидальная сортировка
# Ограничение времени	2 секунды
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Отсортируйте данный массив. Используйте пирамидальную сортировку.
#
# Формат ввода
# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.
#
# Формат вывода
# Выведите эти числа в порядке неубывания.
#
# Пример 1
# Ввод	Вывод
# 1
# 1
# 1
# Пример 2
# Ввод	Вывод
# 2
# 3 1
# 1 3
from typing import List
import sys


class HEAPQmin:
    def __init__(self):
        self.h = []

    def push(self, val):
        self.h.append(val)
        pos = len(self.h) - 1
        while pos > 0 and self.h[pos] < self.h[(pos - 1) // 2]:
            self.h[pos], self.h[(pos - 1) // 2] = self.h[(pos - 1) // 2], self.h[pos]
            pos = (pos - 1) // 2

    def get_min(self):
        min_ = self.h[0]
        self.h[0] = self.h[-1]
        pos = 0
        while (pos * 2) + 2 < len(self.h):
            min_pos = (pos * 2) + 1
            if self.h[min_pos] > self.h[(pos * 2) + 2]:
                min_pos = (pos * 2) + 2
            if self.h[pos] > self.h[min_pos]:
                self.h[pos], self.h[min_pos] = self.h[min_pos], self.h[pos]
            else:
                break
            pos = min_pos
        self.h.pop()
        return min_


def pir_sort(values: List[int], n: int) -> List[int]:
    heapq = HEAPQmin()
    for val in values:
        heapq.push(val)
    values = []
    for _ in range(n):
        values.append(heapq.get_min())
    return values


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    values = list(map(int, input().split()))
    # values = [941, 9837, 1791, 25325, 11037, 9199]
    sys.stdout.write(' '.join([str(v) for v in pir_sort(values, n)]))
