T = int(raw_input())
for t in range(1, T+1):
    N, M = map(int, raw_input().split())
    matrix = []
    for i in range(N):
        matrix.append(map(int, raw_input().split()))

    dp_m = {}

    def get_dp_m(i0, j0, i1, j1):
        if (i0, j0, i1, j1) in dp_m:
            return dp_m[i0,j0,i1,j1]
        if i0 == i1 and j0 == j1:
            dp_m[i0,j0,i1,j1] = matrix[i0][j0]
            return dp_m[i0,j0,i1,j1]
        if i0 == i1:
            dp_m[i0,j0,i1,j1] = min(matrix[i1][j1], get_dp_m(i0, j0, i1, j1-1))
            return dp_m[i0,j0,i1,j1]
        if j0 == j1:
            dp_m[i0,j0,i1,j1] = min(matrix[i1][j1], get_dp_m(i0, j0, i1-1, j1))
            return dp_m[i0,j0,i1,j1]
        dp_m[i0,j0,i1,j1] = min([matrix[i1][j1],
                                 get_dp_m(i0, j1, i1-1, j1),
                                 get_dp_m(i1, j0, i1, j1-1),
                                 get_dp_m(i0, j0, i1-1, j1-1)])
        return dp_m[i0,j0,i1,j1]

    dp = {}

    def get_dp(i0, j0, i1, j1):
        if (i0, j0, i1, j1) in dp:
            return dp[i0,j0,i1,j1]

        ans = 0
        prize = get_dp_m(i0, j0, i1, j1)
        for j in range(j0, j1):
            temp = prize + get_dp(i0, j0, i1, j) + get_dp(i0, j+1, i1, j1)
            if temp > ans:
                ans = temp
        for i in range(i0, i1):
            temp = prize + get_dp(i0, j0, i, j1) + get_dp(i+1, j0, i1, j1)
            if temp > ans:
                ans = temp
        dp[i0,j0,i1,j1] = ans
        
        return dp[i0,j0,i1,j1]

    print "Case #%d: %d" % (t, get_dp(0, 0, N - 1, M - 1))
