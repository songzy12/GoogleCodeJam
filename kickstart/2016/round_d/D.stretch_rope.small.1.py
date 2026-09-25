# https://zibada.guru/gcj/ks2016d/problems/#D


def transform_state(state, A, B, P):
    """Transform a state represented by a bitmask into the 
    corresponding total minimum length, maximum length, and cost.

    Keyword arguments:
    state -- integer representing the state as a bitmask
    A -- list of minimum lengths for each segment
    B -- list of maximum lengths for each segment
    P -- list of costs for each segment
    """
    a, b, c = 0, 0, 0
    i = 0
    while state:
        if state & 1:
            a += A[i]
            b += B[i]
            c += P[i]
        state >>= 1
        i += 1
    return a, b, c


def brute_force(N, M, L, A, B, P, MAXP):
    """Brute force solution to the stretch rope problem.

    Keyword arguments:
    N -- number of segments
    M -- maximum cost
    L -- desired length
    A -- list of minimum lengths for each segment
    B -- list of maximum lengths for each segment
    P -- list of costs for each segment
    """
    cost = MAXP
    for state in range(2**N):
        a, b, c = transform_state(state, A, B, P)
        if c <= M and a <= L <= b:
            cost = min(cost, c)
    return cost


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    P = []
    A = []
    B = []
    for n in range(N):
        a, b, p = map(int, input().split())
        P += p,
        A += a,
        B += b,
    MAXP = sum(P) + 1

    ans = brute_force(N, M, L, A, B, P, MAXP)

    print('Case #%d: %s' % (t, str(ans) if ans != MAXP else 'IMPOSSIBLE'))
