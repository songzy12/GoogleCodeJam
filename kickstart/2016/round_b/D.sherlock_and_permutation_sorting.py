# https://zibada.guru/gcj/ks2016b/problems/#D
#
# Watson is happiest when there are as many chunks as possible; we denote the maximum number of chunks for a permutation p as f(p).
# Watson wants to consider all permutations p of the numbers 1 through N, and find the sum of squares of f(p).


def compute_fact(fact, n, mod):
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod
    return fact


def compute_primitive(size, fact, primitive, mod):
    value = fact[size]
    for suffix_size in range(1, size):
        value = (value - fact[size - suffix_size]
                 * primitive[suffix_size]) % mod
    return value


def compute_sum_f(size, fact, primitive, sum_f, mod):
    total_f = 0
    for suffix_size in range(1, size + 1):
        prefix_size = size - suffix_size
        ways = primitive[suffix_size]

        total_f = (total_f + (sum_f[prefix_size] +
                   fact[prefix_size]) * ways) % mod

    return total_f


def compute_sum_f2(size, fact, primitive, sum_f, sum_f2, mod):
    total_f2 = 0
    for suffix_size in range(1, size + 1):
        prefix_size = size - suffix_size
        ways = primitive[suffix_size]

        total_f2 = (
            total_f2
            + (sum_f2[prefix_size] + 2 *
               sum_f[prefix_size] + fact[prefix_size]) * ways
        ) % mod

    return total_f2


def solve(n, mod):
    if mod == 1:
        return 0

    fact = [1] * (n + 1)
    primitive = [0] * (n + 1)
    sum_f = [0] * (n + 1)
    sum_f2 = [0] * (n + 1)
    primitive[0] = 0

    compute_fact(fact, n, mod)

    for size in range(1, n + 1):
        primitive[size] = compute_primitive(size, fact, primitive, mod)
        sum_f[size] = compute_sum_f(size, fact, primitive, sum_f, mod)
        sum_f2[size] = compute_sum_f2(
            size, fact, primitive, sum_f, sum_f2, mod)

    return sum_f2[n]


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    result = solve(N, M)
    print(f"Case #{t}: {result}")
