T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    m = {}
    for i in range(2*N-1):
        heights = map(int, raw_input().split())
        for height in heights:
            m[height] = m.get(height, 0) + 1
    ans = []
    for t in m:
        if m[t] % 2:
            ans += t,
    for i in sorted(ans):
        print i,
    print
