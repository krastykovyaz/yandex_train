def pref_sum(arr, interval):
    def get_interval(pfs):
        return pfs[interval[1]] - pfs[interval[0]]

    prefsum = 0
    pref_sum_arr = [0]
    for i in range(1, len(arr)):
        sum_in_arr = arr[i - 1]
        prefsum += sum_in_arr
        pref_sum_arr.append(prefsum)
    return get_interval(pref_sum_arr)


if __name__ == '__main__':
    arr = [5,3,8,1,4,6]
    interval = [2,4]
    print(pref_sum(arr, interval))