# https://zibada.guru/gcj/ks2016c/problems/#B
#
# DP
# https://www.geeksforgeeks.org/dsa/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

def count_squares(grid, R, C):
    # 1. count number of squares with bottom right corner at (i, j)
    dp = [[0 for i in range(C + 1)] for j in range(R + 1)]
    for i in range(R, -1, -1):
        for j in range(C, -1, -1):
            if grid[i][j]:
                dp[i][j] = 0
            elif grid[i+1][j] or grid[i][j+1]:
                dp[i][j] = 1
            else:
                # core
                dp[i][j] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1

    # 2. sum up all number of squares
    ans = 0
    for i in range(R+1):
        for j in range(C+1):
            ans += dp[i][j]
    return ans


T = int(input())
for t in range(1, T+1):
    R, C, K = map(int, input().split())
    grid = [[0 for i in range(C+1)] for j in range(R+1)]
    for i in range(R+1):
        grid[i][-1] = 1
    for j in range(C+1):
        grid[-1][j] = 1
    for j in range(K):
        r, c = map(int, input().split())
        grid[r][c] = 1

    ans = count_squares(grid, R, C)
    print("Case #%d: %d" % (t, ans))
