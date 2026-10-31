T = int(raw_input())
for t in range(1, T+1):
    N, TS, TF = [int(x) for x in raw_input().split()]
    params = []
    for n in range(N-1):
        params.append([int(x) for x in raw_input().split()])

    def get_next_time(cur_time, param):
        S, F, D = param
        if cur_time <= S:
            cur_time = S
        passed = (cur_time - S) % F
        return cur_time - passed + D + (F if passed else 0)

    maxn = 16
    maxt = 5000
    # use dp[i][j] as the earliest time that we get to positioin i after visiting j positions
    dp = [[-1 for i in range(maxt+1)] for j in range(maxn+1)]
    for cur_index in range(N-1, -1, -1):
        for cur_time in range(maxt, -1, -1):
            if cur_index == N-1:
                dp[cur_index][cur_time] = -1 if cur_time > TF else 0
            else:
                next_time1 = get_next_time(cur_time, params[cur_index])
                next_time2 = get_next_time(cur_time+TS, params[cur_index])
                temp1 = dp[cur_index+1][next_time1] if next_time1 <= TF else -1
                temp2 = dp[cur_index+1][next_time2] if next_time2 <= TF else -1
                if temp1 == -1 and temp2 != -1:
                    dp[cur_index][cur_time] = temp2 + 1
                elif temp2 == -1 and temp1 != -1:
                    dp[cur_index][cur_time] = temp1
                elif temp1 == -1 and temp2 == -1:
                    dp[cur_index][cur_time] = -1
                else:
                    dp[cur_index][cur_time] = max(temp1, temp2+1) 
                                           

##    dp = {}
##    
##    def get_dp(cur_index, cur_time):
##        if cur_index == N - 1:
##            return -1 if cur_time > TF else 0
##        if (cur_index, cur_time) in dp:
##            return dp[(cur_index, cur_time)]
##        # no sightseeing
##        temp1 = get_dp(cur_index + 1, get_next_time(cur_time, params[cur_index]))
##        temp2 = get_dp(cur_index + 1, get_next_time(cur_time+TS, params[cur_index]))
##        if temp1 == -1 and temp2 != -1:
##            dp[(cur_index, cur_time)] = temp2 + 1
##        elif temp2 == -1 and temp1 != -1:
##            dp[(cur_index, cur_time)] = temp1
##        elif temp1 == -1 and temp2 == -1:
##            dp[(cur_index, cur_time)] = -1
##        else:
##            dp[(cur_index, cur_time)] = max(temp1, temp2+1)
##        return dp[(cur_index, cur_time)]

    def compute():
        ans = dp[0][0]
        if ans == -1:
            return "IMPOSSIBLE"
        return str(ans)

    print "Case #%d: %s" % (t, compute())
        
