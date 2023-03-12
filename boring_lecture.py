import sys
from collections import defaultdict

def get_count(word: str)->None:
    counter_dict = defaultdict(int)
    length = len(word)
    for i in range(len(word)):
        ch = word[i]
        counter_dict[ch] += ((i + 1) * (length - i))
    for k,v in sorted(counter_dict.items(), key=lambda x: x[0]):
        sys.stdout.write(f"{k}: {v}\n")


if __name__=='__main__':
    word = sys.stdin.readline().strip()
    get_count(word)
    # print(get_count(word))