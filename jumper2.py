def get_path(pth, step):
    dp = [0 for _ in range(pth)]
    dp[0] = 1
    for i in range(1, pth):
        r = step
        if r > i: 
            r = i
        for j in range(1, r+1):
            dp[i] = dp[i] + dp[i - j]
    return dp#[-1]




    



if __name__=='__main__':
    pth, step = 8, 3
    print(get_path(pth, step))
