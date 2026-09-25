# https://zibada.guru/gcj/ks2016b/problems/#A
#
# Observation: the pattern ()()() is always best.

def solve(L, R):
    L = min(L, R)
    return L * (L + 1) // 2


T = int(input())
for t in range(1, T + 1):
    L, R = map(int, input().split())
    print(f"Case #{t}: {solve(L, R)}")
