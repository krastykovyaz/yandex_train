# 19. Хипуй
# Ограничение времени	2 секунды
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).
#
# Формат ввода
# В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполнении команды Extract в структуре находится по крайней мере один элемент.
#
# Формат вывода
# Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.
#
# Пример 1
# Ввод	Вывод
# 2
# 0 10000
# 1
# 10000
# Пример 2
# Ввод	Вывод
# 14
# 0 1
# 0 345
# 1
# 0 4346
# 1
# 0 2435
# 1
# 0 235
# 0 5
# 0 365
# 1
# 1
# 1
# 1
# 345
# 4346
# 2435
# 365
# 235
# 5
# 1
class HEAPQ:
    def __init__(self):
        self.heapq = []

    def insert(self, val):
        self.heapq.append(val)
        pos = len(self.heapq) - 1
        while pos > 0 and val > self.heapq[(pos - 1) // 2]:
            if val > self.heapq[(pos - 1) // 2]:
                self.heapq[pos], self.heapq[(pos - 1) // 2] = self.heapq[(pos - 1) // 2], self.heapq[pos]
            pos = (pos - 1) // 2

    def extract(self):
        root = self.heapq[0]
        self.heapq[0] = self.heapq[-1]
        pos = 0
        while (2 * pos) + 2 < len(self.heapq):
            max_pos = (2 * pos) + 1
            if self.heapq[(2 * pos) + 2] > self.heapq[(2 * pos) + 1]:
                max_pos = (2 * pos) + 2
            if self.heapq[pos] < self.heapq[max_pos]:
                self.heapq[max_pos], self.heapq[pos] = self.heapq[pos], self.heapq[max_pos]
            else:
                break
            pos = max_pos
        self.heapq.pop()
        return root



if __name__ == '__main__':
    h = HEAPQ()
    n = int(input())
    for _ in range(n):
        move = list(map(int, input().split()))
        if move[0] == 0:
            h.insert(move[1])
        else:
            print(h.extract())
        # print(h.heapq)


# 2, 5, 4, 11, 6, 8, 25