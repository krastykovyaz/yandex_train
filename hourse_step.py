def get_steps(n, m):
    dp = [(m) * [0] for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            if i >= 2 and j >= 1:
                dp[i][j] += dp[i-2][j-1]
            if i >= 1 and j >= 2:
                dp[i][j] += dp[i-1][j-2]
    return dp, dp[n-1][m-1]

if __name__=='__main__':
    n, m = tuple(map(int, input().split()))
    print(get_steps(n, m))
