from typing import List

def merge(arr1: List[int], arr2: List[int])->List[int]:
    sorted_list = [0] * (len(arr1) + len(arr2))
    first, last = 0, 0
    for k in range(len(arr1) + len(arr2)):
        if first < len(arr1) and arr1[first] < arr2[last]:
            sorted_list[k] = arr1[first]
            first += 1
        else:
            sorted_list[k] = arr2[last]
            last += 1
    return sorted_list


if __name__=='__main__':
    arr1 = [1,2,5,7,8, 8]
    arr2 = [3,4,6,9,10]
    print(merge(arr1, arr2))