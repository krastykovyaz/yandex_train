from typing import List

def is_acs(a: List[int])->bool:
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return -1
    return a[-1] - a[0]




if __name__=='__main__':
    # n = int(input())
    a = [1, 10, 5, 5, 5]
    print(is_acs(a))