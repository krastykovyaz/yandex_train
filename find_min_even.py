from typing import List
def find_min_even(seq: List[int])->int:
    minim = -1
    for i in range(len(seq)):
        if minim >  seq[i] and seq[i] % 2 == 0:
            minim = seq[i]
    return minim

if __name__=='__main__':
    sequece = [7,5,3,9,9,5,3]
    print(find_min_even(sequece))
    assert find_min_even(sequece) == -1