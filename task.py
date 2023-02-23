# a = [] increase
# b = [] increase
# k = ?
# i, j пары такие ai + bj = k
from typing import List, Union

def bin_search(b: List[int], m: int)->Union[None, int]:
    mid = len(b) // 2
    if b[mid] == m:
        return b[mid]
    elif len(b) == 1:
        return
    elif m < b[mid]:
        bin_search(b[:mid], m)
    else:
        bin_search(b[mid:], m)

def find_pairs(a: List[int], b: List[int], k: int) -> List[tuple]:
    collect = []
    for i in range(len(a)):
        k_ = k - a[i]
        match = bin_search(b, k_)
        if match is not None:
            collect.append((a[i], match))
    return collect


if __name__=='__main__':
    a = [1,3,4,7]
    b = [5,7,9,11]
    k = 10
    print(find_pairs(a,b,k))
    assert [(1,9),(3,7)] == find_pairs(a,b,k)
    