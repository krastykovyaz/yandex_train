# 23. Калькулятор
# Ограничение времени	2 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Имеется калькулятор, который выполняет следующие операции:
#
# умножить число X на 2;
# умножить число X на 3;
# прибавить к числу X единицу.
# Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.
#
# Формат ввода
# Во входном файле написано натуральное число N, не превосходящее 106.
#
# Формат вывода
# В первой строке выходного файла выведите минимальное количество операций. Во второй строке выведите числа, последовательно получающиеся при выполнении операций. Первое из них должно быть равно 1, а последнее N. Если решений несколько, выведите любое.
#
# Пример 1
# Ввод	Вывод
# 1
# 0
# 1
# Пример 2
# Ввод	Вывод
# 5
# 3
# 1 3 4 5

def calc(n:int)->str:
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    prev = [0] * (n + 1)
    for i in range(2, n+1):
        if dp[i-1] < dp[i]:
            dp[i] = dp[i-1] + 1
            prev[i] = i-1
        if i % 2 == 0 and dp[i//2] < dp[i]:
            dp[i] = dp[i//2] + 1
            prev[i] = i//2
        if i % 3 == 0 and dp[i//3] < dp[i]:
            dp[i] = dp[i//3] + 1
            prev[i] = i//3
    print(dp[n])
    seq = []
    cur = n
    while cur != 0:
        
        seq.append(cur)
        cur = prev[cur]



    return seq[::-1]


if __name__=='__main__':
    n = int(input())
    print(*calc(n))