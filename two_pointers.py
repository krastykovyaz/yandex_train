def diff_k(arr, k):
    pref = 0
    j = 1
    for i in range(1, len(arr)):
        while j < len(arr) and k >= arr[j] - arr[i-1]:
            j += 1
        pref += len(arr) - j
    return pref




if __name__=='__main__':
    arr = [1,3,5,6,7,10,11,13,15]
    k = 4
    print(diff_k(arr, k))