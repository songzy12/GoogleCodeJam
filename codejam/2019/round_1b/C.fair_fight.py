# 先暴力一发算了

T = int(input())

def solve(N, K, C, D):
    cnt = 0
    for L in range(N):
        maxc = 0
        maxd = 0
        for R in range(L, N):            
            maxc = max(maxc, C[R])
            maxd = max(maxd, D[R])
            if abs(maxc - maxd) <= K:
                cnt += 1
    return cnt

for t in range(1, T+1):
    N , K  = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    print("Case #%d: %d" % (t, solve(N, K, C, D)))

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838