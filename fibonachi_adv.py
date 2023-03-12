


if __name__=='__main__':
    n = 3
    dp = [-1 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1
    def fnum(n, dp):
        if dp[n] == -1:
            dp[n] = fnum(n-1, dp) + fnum(n-2, dp)
        return dp[n]
    print(fnum(n, dp))