def count_cuts(arr):
    pref = 0
    pref_dict  = {0:1}
    for i in range(1, len(arr)):
        pref += arr[i - 1]
        if pref not in pref_dict:
            pref_dict[pref] = 0
        pref_dict[pref] += 1
    count_range = 0
    for k in pref_dict:
        count_rows = pref_dict[k]
        count_range += count_rows * (count_rows - 1) // 2
    return count_range

if __name__=='__main__':
    arr = [1,0,0,8,7,6,6,7,7,7,8,8]
    print(count_cuts(arr))