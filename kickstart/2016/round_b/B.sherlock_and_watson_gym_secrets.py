# https://zibada.guru/gcj/ks2016b/problems/#B
#
# Input: A, B, N, K
# Output: Number of pairs (i, j) such that
#   (i^A + j^B) % K == 0 and i != j
# for i, j in range [1, N]
#
# [1^A, 2^A, 3^A, ..., K^A] % K
# [1^B, 2^B, 3^B, ..., K^B] % K

from collections import defaultdict

MOD = 10**9 + 7


def fast_pow(x, n, K):
    """Computes (x^n) % K using binary exponentiation."""
    res = 1
    while n:
        if n & 1:
            res = (res * x) % K
        x = (x * x) % K
        n >>= 1
    return res % K


def compute_mod_index_map(K, A):
    """Computes a map from (i^A % K) to list of indices i."""
    mod_index_map = defaultdict(set)
    for i in range(1, K + 1):
        mod_index_map[fast_pow(i, A, K)].add(i)
    return mod_index_map


def filter_mod_index_map(mod_index, indices):
    filtered_mod_index = defaultdict(set)
    for k, index_set in mod_index.items():
        filtered_mod_index[k] = set(filter(lambda x: x <= indices, index_set))
    return filtered_mod_index


def compute_hits(mod_index_a, mod_index_b, K):
    total_pairs = 0
    for mod_a in mod_index_a:
        target_mod_b = (K - mod_a) % K  # Here "% K" since K can be 1

        total_pairs += len(mod_index_a[mod_a]) * len(mod_index_b[target_mod_b])
        total_pairs %= MOD
    return total_pairs % MOD


def compute_duplications(mod_index_a, mod_index_b, K):
    total_pairs = 0
    for mod_a in mod_index_a:
        target_mod_b = (K - mod_a) % K

        total_pairs += len(mod_index_a[mod_a].intersection(
            mod_index_b[target_mod_b]))
        total_pairs %= MOD
    return total_pairs % MOD


def compute_full_cycles(mod_index_a, mod_index_b, K, full_cycles):
    if full_cycles == 0:
        return 0
    hits = compute_hits(mod_index_a, mod_index_b,
                        K) * full_cycles * full_cycles
    duplications = compute_duplications(mod_index_a, mod_index_b,
                                        K) * full_cycles
    # print(f"hits: {hits}")
    # print(f"duplications: {duplications}")
    return (hits - duplications) % MOD


def compute_full_cycle_with_remainder(mod_index_a, mod_index_b, K, full_cycles,
                                      remainder):
    if full_cycles == 0 or remainder == 0:
        return 0

    filtered_mod_index_b = filter_mod_index_map(mod_index_b, remainder)

    hits = compute_hits(mod_index_a, filtered_mod_index_b, K) * full_cycles
    # print(f"hits: {hits}")
    return hits % MOD


def compute_remainders(mod_index_a, mod_index_b, K, remainder):
    if remainder == 0:
        return 0

    filtered_mod_index_a = filter_mod_index_map(mod_index_a, remainder)
    filtered_mod_index_b = filter_mod_index_map(mod_index_b, remainder)

    hits = compute_hits(filtered_mod_index_a, filtered_mod_index_b, K)
    duplications = compute_duplications(filtered_mod_index_a,
                                        filtered_mod_index_b, K)
    # print(f"hits: {hits}")
    # print(f"duplications: {duplications}")
    return (hits - duplications) % MOD


def compute_pairs(mod_index_a, mod_index_b, K, N):
    full_cycles = (N // K) % MOD
    remainder = N % K
    # print(f"full_cycles: {full_cycles}, remainder: {remainder}")
    return compute_full_cycles(mod_index_a, mod_index_b, K, full_cycles) + \
        compute_remainders(mod_index_a, mod_index_b, K, remainder) + \
        compute_full_cycle_with_remainder(mod_index_a, mod_index_b, K, full_cycles, remainder) + \
        compute_full_cycle_with_remainder(
            mod_index_b, mod_index_a, K, full_cycles, remainder)


def solve(K, A, B, N):
    mod_index_a = compute_mod_index_map(K, A)
    mod_index_b = compute_mod_index_map(K, B)
    return compute_pairs(mod_index_a, mod_index_b, K, N) % MOD


T = int(input())
for t in range(1, T + 1):
    A, B, N, K = map(int, input().split())
    print(f"Case #{t}: {solve(K, A, B, N)}")
