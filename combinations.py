# Сочетания
# Выведите число сочетаний 
# C(n,k).

# Формат ввода
# В первой строке находится два числа 
# (1≤n≤7), 
# (1≤k≤7).

# Формат вывода
# Выведите ответ на задачу.

# Пример 1
# Ввод
# 3 2
# Вывод
# 3
# Пример 2
# Ввод
# 7 5
# Вывод
# 21
# Пример 3
# Ввод
# 1 1
# Вывод
# 1
# Ограничение памяти
# 256.0 Мб
# Ограничение времени
# 1 с
# Ввод
# стандартный ввод или input.txt
# Вывод
# стандартный вывод или output.txt

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)

def main(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * (factorial(n - k))
    return int(numerator / denominator)


from itertools import combinations

def count_combinations(n, k):
    """
    Count combinations of selecting k elements from n elements.

    Args:
        n (int): Total number of elements.
        k (int): Number of elements to select.

    Returns:
        int: Number of combinations.
    """
    return len(list(combinations(range(1, n + 1), k)))


if __name__=='__main__':
    vals = list(map(int, input().split()))
    n, k = vals
    print(main(n, k))