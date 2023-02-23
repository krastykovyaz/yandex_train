from typing import List


def get_max(n: int, a: List[str]) -> int:
    def count_ch(chars: List[str], add: int) -> int:
        res = 0
        for i in range(1, len(chars)):
            count = 1
            j = i
            while j < len(chars) and chars[j - 1] == chars[j]:
                count += 1
                j += 1
            if res < count:
                res = count
        remain = len(chars) - res
        return res + min(add, remain)

    max_count = 0
    values = set(a)
    for value in sorted(values):
        i = 0
        while i < len(a) - n:
            tmp_a = list(a)
            slice = list(value * n)
            len_char = len([ch for ch in tmp_a[i:i + n] if value == ch])
            tmp_a[i:i + n] = slice
            max_count_new = count_ch(tmp_a, len_char)
            if max_count < max_count_new:
                max_count = max_count_new
            i += 1
    return max_count


if __name__ == '__main__':
    n = 2
    string = "helto"
    print(get_max(n, string))
