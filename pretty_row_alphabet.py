import sys
from typing import List
from collections import defaultdict
def good_alpha(numbers: List[int])->int:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = defaultdict(int)
    return  min(numbers) * (len(numbers) - 1)




if __name__ =='__main__':
    n = sys.stdin.readline()
    numbers = []
    for _ in range(int(n)):
        numbers.append(int(sys.stdin.readline()))
    sys.stdout.write(str(good_alpha(numbers)))