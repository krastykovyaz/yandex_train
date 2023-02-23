from typing import List
def find_max(seq: List[int])->int:
    maxim = seq[0]
    for i in range(1, len(seq)):
        if maxim < seq[i]:
            maxim = seq[i]
    return maxim
        

if __name__== '__main__':
    sequence = [1,6,4,-1,3,4,5,6,2,7,8,0]
    print(find_max(sequence))
    assert find_max(sequence) == 8