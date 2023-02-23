# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E. Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.
#
# Формат ввода
# Программа получает на вход числа A, B, C, D, E.
from typing import List

def is_free()->str:
    A, B, C, D, E = [input() for _ in range(5)]
    maxim = max(A, B, C)
    minim = min(A, B, C)
    for val in (A, B, C):
        if minim <= val <= maxim:
            middle = val
    D, E = min(D, E), max(D, E)
    if D <= E and D >= minim and E >= middle:
        return 'OK'
    else:
        return 'NO'

if __name__=='__main__':
    print(is_free())


