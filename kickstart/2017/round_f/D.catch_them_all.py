T = int(raw_input())

dp = [i for i in range(10005)]

for n in range(10005):
    for i in range(1, n):
        if i * i > n:
            break
        dp[n] = min(dp[n], 1 + dp[n - i*i])
        
for t in range(1, T+1):
    N = int(raw_input())
    print "Case #%d: %d" % (t, dp[N])

