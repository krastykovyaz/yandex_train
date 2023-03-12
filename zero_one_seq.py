# По данному числу N определите количество последовательностей из нулей и единиц длины N, в которых никакие три единицы не стоят рядом.
#
# Формат ввода
# Во входном файле написано натуральное число N, не превосходящее 35.
#
# Формат вывода
# Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 231-1.
#
# Пример
# Ввод	Вывод
# 1
# 2

def get_seq_as_fib(n: int)->int:
    dp = [0 for _ in range(n+3)]
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 7
    dp[0], dp[1], dp[2], dp[3] = 1, 2, 4, 7
    for i in range(4, n+1):
        r = 4
        if i < r:
            r = i
        for j in range(1, r):
            dp[i] = dp[i] + dp[i - j]

    return dp[n]

def get_seq_as_fib2(n: int)->int:
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 7
    return get_seq_as_fib2(n-1) + get_seq_as_fib2(n-2) + get_seq_as_fib2(n-3)


if __name__=='__main__':
    n = int(input())
    # for n in range(1, 35):
    #     assert get_seq_as_fib2(n)==get_seq_as_fib(n)
    print(get_seq_as_fib(n))
