def find_freq_char(sequence: str)->str:
    symbols = {}
    maxim = 0
    res = None
    for c in sequence:
        if c not in symbols:
            symbols[c] = 0
        symbols[c] += 1    
        if symbols[c] > maxim:
            res = c
            maxim = symbols[c]
    return res

        

if __name__=='__main__':
    string = 'dfcghvjknlm;,kmjnbhgvfcdghrecrgrr'
    print(find_freq_char(string))
