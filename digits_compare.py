from typing import List


def is_same(l1: List[int], l2: List[int]) -> bool:
    def create_dict(hash, l):
        while l:
            last = l % 10
            hash[last] += 1
            l //= 10
        return hash


    counter1 = [0 for _ in range(9)]
    counter2 = [0 for _ in range(9)]
    counter1 = create_dict(counter1, l1)
    counter2 = create_dict(counter2, l2)
    return counter1 == counter2


if __name__ == '__main__':
    arr1 = 3452
    arr2 = 5432
    print(is_same(arr1, arr2))
