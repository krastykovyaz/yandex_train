import sys
from typing import List

def relocate(cities: List[int], m: int)->List[int]:
    new_positions = []
    for i in range(m):
        j = i
        pos = -1
        while j < m:
            if cities[i] > cities[j]:
                pos = j
                break
            j += 1
        new_positions.append(pos)
    return new_positions

if __name__=='__main__':
    m = int(sys.stdin.readline())
    cities = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(' '.join([str(el) for el in relocate(cities, m)]))

