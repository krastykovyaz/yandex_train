from typing import List

def max_mult(numbers: List[int], x: int):
    mid = len(seq) // 2
    def k_stat(seq, left, right, k):
        for i in range(len(seq) - 1, len(right), -1):
            if seq[left] > seq[i]:
                seq[left], seq[right] = seq[right], seq[left]
                seq[right], seq[i] = seq[i], seq[right]
                left += 1
                right += 1
            elif seq[right] == seq[i]:
                seq[right], seq[i] = seq[i], seq[right]
                right += 1
            # print(seq[i])
        return seq
    sorted = k_stat(seq, 0, mid, x)
    return sorted




if __name__=='__main__':
    seq = [0,3,4,5,2,6,9,8]
    print(max_mult(seq, 3))