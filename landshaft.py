from typing import List

def get_water(seq: List[int])->int:
    start = seq[0]
    count = 0
    maxim = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > seq[maxim]:
            maxim = i
    for i in range(1, len(seq)):
        if i < maxim:
            if start > seq[i]:
                count += (start  - seq[i])
            else:
                start = seq[i]
    finish = seq[len(seq) - 1]
    for j in range(len(seq) - 2, 0, -1):
        if j > maxim:
            if finish > seq[j]:
                count += (finish - seq[j])
            else:
                finish = seq[j]
    return count

        

if __name__=='__main__':
    seq = [2, 1, 3, 2, 3, 1, 2]
    print(get_water(seq))
    assert get_water(seq) == 3