from typing import List
def find_first(seq: List[int], z: int)->int:
    idx = -1
    for i in range(len(seq)):
        if seq[i] == z:
            return i
    return idx

if __name__=='__main__':
    sequece = [4,5,3,2,4,5,3]
    num = 2
    print(find_first(sequece, num))
