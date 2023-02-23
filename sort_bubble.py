from typing import List


def sort_(values: List[int]) -> List[int]:
    for j in range(1, len(values)):
        for i in range(1, len(values)):
            if values[i - 1] > values[i]:
                    values[i - 1], values[i] = values[i], values[i - 1]
    return values

if __name__=='__main__':
    arr = [1,22,30,8,7,6,5,4,3,2]
    print(sort_(arr))
