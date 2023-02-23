from typing import List

def find_in_dict(seq: List[str], text: str)->bool:
    for s in seq:
        for i in range(1, len(s) + 1):
            if s[:i - 1] + s[i:] == text:
                return True
    return False

if __name__=='__main__':
    sequence = ['abcd', 'vybguhn', 'gbhn', 'mjnh']
    text = 'mjn'
    print(find_in_dict(sequence, text))
