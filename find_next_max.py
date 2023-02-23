from typing import List
def find_max(seq: List[int])->int:
    maxim_f = seq[0]
    maxim_s = seq[1]
    for i in range(len(seq)):
        if maxim_f < seq[i]:
            maxim_f, maxim_s = seq[i], maxim_f
    return maxim_s


if __name__== '__main__':
    sequence = [1,6,4,3,4,5,6,2,7,8,0]
    print(find_max(sequence))
    assert find_max(sequence) == 7