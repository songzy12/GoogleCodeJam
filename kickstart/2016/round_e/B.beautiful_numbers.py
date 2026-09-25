# https://zibada.guru/gcj/ks2016e/problems/#B


def binary_search(f, target, low, high):
    """
    Find the largest integer x in [low, high) such that f(x) <= target.
    """
    while low < high:
        mid = (low + high) // 2
        if f(mid) < target:
            low = mid + 1
        else:
            high = mid
    return high


def is_beautiful(N, x):
    """
    Check whether there is a base b such that N is a beautiful number in base b and has x digits.

    This means for certain x, we have N = 1 + b + b^2 + ... + b^(x-1) = (b^x - 1) / (b - 1).

    Note that f(x) = (b^x - 1) / (b - 1) is a monotone increasing function of b, and f(1) = 1, f(N+1) > N.
    So we can find the base b by binary search.

    return: A tuple (hit, b) where hit is a boolean indicating whether such a base exists, and b is the base if it exists.
    """
    b = binary_search(f=lambda b: (b**x - 1) // (b - 1),
                      target=N, low=2, high=N-1)
    return b**x - 1 == N * (b - 1), b


def solve(N):
    """
    Find the smallest base b (b >= 2) such that N is a beautiful number in base b.
    A beautiful number in base b is defined as a number that can be represented
    as a sequence of 1's in that base.

    This means for certain x, we have N = 1 + b + b^2 + ... + b^(x-1) = (b^x - 1) / (b - 1).
    This is equivalent to check whether x = log_b(N * (b - 1) + 1) is an integer.

    On the other hand, notice that the minimum value of b is 2, which means 
    the maximum value of x is log_2(N * (b - 1) + 1) <= log_2(10^18 * 1 + 1) < 60.

    param N: The number to check. Scope: 1 <= N <= 10^18.
    return: The smallest base b such that N is a beautiful number in base b.
    """
    x = 64
    while x > 1:
        hit, b = is_beautiful(N, x)
        if hit:
            return b
        x -= 1
    return N - 1


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        ans = solve(N)
        print('Case #%d: %d' % (t, ans))
