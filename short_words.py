from typing import List

def get_short_words(seq: List[str]) -> str:
    short_words = [seq[0]]
    for i in range(len(seq)):
        if len(short_words[-1]) > len(seq[i]):
            short_words = [seq[i]]
        elif len(short_words[-1]) == len(seq[i]):
            short_words.append(seq[i])
    return ' '.join(short_words)


if __name__=='__main__':
    seq = ['aa', 'ab', 'gccc', 'fd', 'f', 's', 'cwer']
    print(get_short_words(seq))