

def fnum(n: int)->int:
    dp = [0] * n
    if len(dp) < 2:
        return 1
    dp[0] = 1
    dp[1] = 1
    # if n == 0 or n == 1:
    #     return 1
    for i in range(1, n):
        r = 2
        if i < r:
            r = i
        for j in range(1, r + 1):
            dp[i] = dp[i-j] + dp[i]
    return dp[-1]
    # return fnum(n-1) + fnum(n-2)

def f_num(n: int)->int:
    if n == 0 or n ==1:
        return 1
    return f_num(n-1) + f_num(n-2)

if __name__=='__main__':
    for num in range(100):
        assert fnum(num) == f_num(num)