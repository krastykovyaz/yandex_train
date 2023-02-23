from typing import List


def mirror_seq(seq: List[int]) -> List[int]:
    def is_polen(sequ, idx):
        j = 0
        for i in range(len(sequ) - 1, idx, -1):
            if sequ[i] != sequ[j]:
                return False
            j += 1
        return True
    count_each_seq = []
    for i in range(0, len(seq)):
        z = i
        j = 0
        while j < len(seq) and j < i and z < len(seq) and seq[z] == seq[j]:
            z += 1
            j += 1
        count_each_seq.append(z - i)
    max_idx = count_each_seq.index(max(count_each_seq))
    res = is_polen(seq, max_idx)
    if res:
        return seq


if __name__ == '__main__':
    a = [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    answer = [0, 0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 3, 0, 1]
    print(mirror_seq(a))
    # assert mirror_seq(a) == answer
