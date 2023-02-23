from typing import List

def push_zeros(arr: List[int])->List[int]:
    def swap(a: int, b: int):
        a, b = b, a
        return a, b

    for i in range(1, len(arr)):
        if arr[i - 1] == 0:
            j = i
            while j < len(arr):
                arr[j - 1], arr[j] = swap(arr[j - 1], arr[j])
                j += 1
    i = len(arr) - 1
    while arr[i] == 0:
        arr.pop()
        i -= 1





if __name__=='__main__':
    arr = [0, 9, 8, 7, 0, 4, 9, 0, 2]
    push_zeros(arr)
    print(arr)