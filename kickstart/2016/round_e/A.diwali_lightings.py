# https://zibada.guru/gcj/ks2016e/problems/#A

def compute_prefix(S, I):
    L = len(S)
    div, mod = I // L, I % L
    return S.count('B') * div + S[:mod].count('B')


def compute(S, I, J):
    return compute_prefix(S, J) - compute_prefix(S, I-1)


T = int(input())
for t in range(1, T+1):
    S = input()
    I, J = map(int, input().split())
    ans = compute(S, I, J)
    print('Case #%d: %d' % (t, ans))
