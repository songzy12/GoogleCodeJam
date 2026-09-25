# https://zibada.guru/gcj/ks2016d/problems/#D

from dataclasses import dataclass
from typing import List

@dataclass
class ProblemData:
    N: int  # Number of ropes
    M: int  # Maximum total cost allowed
    L: int  # Target length to reach or exceed
    A: List[int]  # Minimum length of each rope
    B: List[int]  # Maximum length of each rope
    P: List[int]  # Cost of each rope
    MAXP: int  # Infinity value for cost (sum of all costs + 1)

def dfs(index, cur_min_l, cur_max_l, cur_cost, data: ProblemData):
    if cur_cost > data.M:
        return data.MAXP
    if data.L < cur_min_l:
        return data.MAXP
    if data.L <= cur_max_l:
        return cur_cost
    if index == data.N:
        return data.MAXP

    cost_skip = dfs(index+1, cur_min_l, cur_max_l, cur_cost, data)
    cost_nonskip = dfs(
        index+1, cur_min_l+data.A[index], cur_max_l+data.B[index], cur_cost+data.P[index], data)
    return min(cost_nonskip, cost_skip)


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    A = []
    B = []
    P = []
    for n in range(N):
        a, b, p = map(int, input().split())
        A += a,
        B += b,
        P += p,
    MAXP = sum(P) + 1

    data = ProblemData(N, M, L, A, B, P, MAXP)
    ans = dfs(0, 0, 0, 0, data)

    print('Case #%d: %s' % (t, str(ans) if ans != MAXP else 'IMPOSSIBLE'))
