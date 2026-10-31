T = int(input())


def solve(N, K, A):
    A.sort()
    res = 0
    cur_day = 1
    while A:
        while A and A[0] < cur_day:
            A.pop(0)
        while A and res < cur_day * K:
            res += 1
            A.pop(0)
        cur_day += 1

    return res

for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print("Case #%d: %d" % (t, solve(N, K, A)))
