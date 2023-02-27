from typing import List
import sys


def get_max(n: int, a: List[str]) -> int:
    count_list = []
    for l in range(len(a)):
        r = l
        count = 0
        k = n
        while r < len(a):
            if a[r] == a[l]:
                count += 1
            elif k:
                count += 1
                k -= 1
            else:
                break
            r += 1
        count_list.append(count)
    return max(count_list)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    string = sys.stdin.readline()
    sys.stdout.write(str(get_max(n, string)))
