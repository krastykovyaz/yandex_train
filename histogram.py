def histogram(s: str) -> None:
    str_dict = {}
    max_count = 0
    for c in s:
        if c not in str_dict:
            if c ==',':
                print('f')
            str_dict[c] = 1
        str_dict[c] += 1
        max_count = max(max_count, str_dict[c])
    sorted_str_dict = sorted(str_dict.keys())
    for floor in range(max_count, 1, -1):
        for k in sorted_str_dict:
            if str_dict[k] >= floor:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print(''.join(sorted_str_dict), end='')


if __name__ == '__main__':
    s = """Twas brillig, and the slithy toves
            Did gyre and gimble in the wabe;
            All mimsy were the borogoves,
            And the mome raths outgrabe."""
    histogram(s)
