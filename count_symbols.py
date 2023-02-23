from typing import List

def cut_symbols(seq: str)->str:
    if seq == '':
        return ''
    seq += '_' if seq[-1] != '_' else '^'
    start = seq[0]
    count = 1
    res = []
    for i in range(1, len(seq)):
        if seq[i] == start:
            count += 1
        else:
            res.append(start)
            if count > 1:
                res.append(count)
            start = seq[i]
            count = 1
    return ''.join(str(c) for c in res)
            



if __name__=='__main__':
    string = "aabbccc"
    print(cut_symbols(string))