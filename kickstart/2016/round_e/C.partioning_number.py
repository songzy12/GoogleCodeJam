# https://zibada.guru/gcj/ks2016e/problems/#C
#
# Find the number of tuples (a, b, c, x) such that:
#   a*x + b*(x+1) + c*(x+2) = N, where
#   1. a, b, c, x are non-negative integers
#   2. D | x
#   3. a >= 1
#
# Also, https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm


def compute_solution_count(N, a, x):
    """
    Compute the number of tuples (b, c) such that:
    1. a*x + b*(x+1) + c*(x+2) = N
    2. b, c are non-negative integers

    That is:

    (x+1)*b + (x+2)*c = N - a*x

    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    https://www.geeksforgeeks.org/python/python-program-for-basic-and-extended-euclidean-algorithms-2/
    """

    if N - a*x < 0:
        return 0
    # Here is how we compute an initial solution (b0, c0).
    # Note: gcd(x+1, x+2) = 1, that means:
    #   (-1, 1) * (N - a*x) is a solution of (b, c)
    #
    # All solutions would be (-(N-a*x) + t*(x+2), N-a*x - t*(x+1))
    #
    # We need to find the number of t such that:
    # 1. -(N-a*x) + t*(x+2) >= 0
    # 2. N-a*x - t*(x+1) >= 0
    # That is:
    # * (N-a*x) / (x+1) >= t >= (N-a*x) / (x+2)
    start = (N - a*x) // (x+2)
    if (N - a*x) % (x+2) != 0:
        start += 1
    end = (N - a*x) // (x+1)
    return end - start + 1


def solve(N, D):
    ans = 0
    for x in range(D, N+1, D):
        for a in range(1, N//x+1):
            ans += compute_solution_count(N, a, x)
    return ans


T = int(input())
for t in range(1, T+1):
    N, D = map(int, input().split())
    ans = solve(N, D)
    print('Case #%d: %d' % (t, ans))
