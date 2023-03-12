import sys
from typing import List
import random

def get_square(coordinates: List[int]) -> List[int]:
    max_x, min_x, max_y, min_y = 1, 1, 1, 1
    f_max = lambda item_max, item: item_max if item < item_max else item
    f_min = lambda item_min, item: item if item < item_min else item_min
    for x, y in coordinates:
        max_x, min_x, max_y, min_y = \
            f_max(max_x, x), f_min(min_x, x), \
            f_max(max_y, y), f_min(min_y, y)
    return f"{min_x} {min_y} {max_x} {max_y}"


def get_square2(coordinates: List[int]) -> List[int]:
    xx = [x for x, _ in coordinates]
    yy = [y for _, y in coordinates]
    return f"{min(xx)} {min(yy)} {max(xx)} {max(yy)}"


if __name__ == '__main__':
    # k = int(sys.stdin.readline())
    for k in range(1, 100):
        # coordinates = []
        coordinates = ([(random.randint(1, 10 ** 9), random.randint(1, 10 ** 9)) for el in range(k)])
        # for _ in range(k):
        #     coordinates.append(tuple(map(int, sys.stdin.readline().split())))
        print(get_square2(coordinates), get_square(coordinates))
        assert get_square2(coordinates) == get_square(coordinates)
