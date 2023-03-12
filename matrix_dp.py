import sys
def get_min_cost(mapp, n, m):
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = mapp[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] +mapp[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1]+mapp[0][j]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + mapp[i][j]
    path = []
    i, j = n - 1, m - 1
    print(dp)
    while i > 0 or j > 0:
        if (i > 0 and dp[i - 1][j] > dp[i][j-1]) or j == 0:
            path.append('D')
            i -= 1
        if (j > 0 and dp[i - 1][j] < dp[i][j-1]) or i == 0:
            path.append('R')
            j -= 1
        print(path)
        if j == 1:
            print(i)
            break
    return f"{dp[n-1][m-1]}\n{' '.join(path[::-1])}"


if __name__=='__main__':
    # payload = '''5 5
    # 1 1 1 1 1
    # 3 100 100 100 100
    # 1 1 1 1 1
    # 2 2 2 2 1
    # 1 1 1 1 1'''
    # data = payload.split('\n')
    n, m = list(map(int, sys.stdin.readline().split()))
    mapp = []
    for _ in range(m):
        line = sys.stdin.readline()
        mapp.append(list(map(int, line.strip().split())))
    # print(mapp)
    print(get_min_cost(mapp, n, m))