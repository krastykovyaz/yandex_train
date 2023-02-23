def prefix_zero(arr):
    pref = 0
    pref_zeros = [0]
    for i in range(1, len(arr)):
        if arr[i-1] == 0:
            pref += 1
        pref_zeros.append(pref)
    return pref_zeros

if __name__ == '__main__':
    arr = [1, 0, 1, 1, 0, 0, 1]
    print(prefix_zero(arr))

