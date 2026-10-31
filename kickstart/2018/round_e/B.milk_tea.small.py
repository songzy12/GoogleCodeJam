T = int(input())


def solve(p, f, P):
    res = None

    p = list(map(lambda x: int(x, 2), p))
    f = list(map(lambda x: int(x, 2), f))
    for case in range(1 << P):
        if case in f:
            continue
        temp = 0
        for a in p:
            temp += sum(map(int, bin(a ^ case)[2:]))
        if res == None:
            res = temp
        if temp < res:
            res = temp
    return res

for t in range(1, T + 1):
    N, M, P = map(int, input().split())
    p = []
    for n in range(N):
        p.append(input())
    f = []
    for m in range(M):
        f.append(input())
    print("Case #%d: %d" % (t, solve(p, f, P)))

