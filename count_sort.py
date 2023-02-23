from typing import List

def sort_counted(seq: List[int])->List[int]:
    maxim = max(seq)
    minim = min(seq) 
    tmp_seq = [0 for _ in range(minim - 1, maxim)]
    for s in seq:
        i = s - minim
        tmp_seq[i] += 1
    i = 0
    count = 0
    while i < len(tmp_seq):
        if tmp_seq[i]:
            add = [i + minim for _ in range(tmp_seq[i])]
            length = len(add)
            seq[count:count + length] = add
            count += length
        i += 1
    return seq

if __name__=='__main__':
    sequence = list(map(int, list('546789876543567899876543678')))
    print(sort_counted(sequence))