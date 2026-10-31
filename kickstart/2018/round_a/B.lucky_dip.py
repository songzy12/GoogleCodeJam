T = int(input())

from bisect import bisect_right

def solve(V, K, N):
    dp = [0 for i in range(K+1)]
    
    prefix = [0 for i in range(len(V)+1)]
    for i in range(len(V)):
        prefix[i+1] = prefix[i] + V[i]
    
    dp[0] = sum(V) / len(V)
    for k in range(1, K+1):
        index = bisect_right(V, dp[k-1])
        # this is the index that are first smaller than V
        if index == N:
            dp[k] = dp[k-1]
            continue
        dp[k] = index / N * dp[k-1] + \
                (1 - index / N) * (prefix[-1] - prefix[index]) / (N - index)
    return dp[-1]

for t in range(1, T+1):
    N, K = map(int, input().split())
    V = sorted(list(map(int, input().split())))
    print("Case #%d: %.6f" %(t, solve(V, K, N)))
