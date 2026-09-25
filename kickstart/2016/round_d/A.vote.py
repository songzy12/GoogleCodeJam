# https://zibada.guru/gcj/ks2016d/problems/#A
#
# This is exactly: https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ans = (N - M) * 1.0 / (M + N)
    print('Case #%d: %.8f' % (t, ans))
