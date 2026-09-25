# https://zibada.guru/gcj/ks2016d/problems/#D
#
# https://codeforces.com/blog/entry/47796
#
# Main: DP
#   Let dp[n][L] = the least money to create a rope of exactly size L, using the first n ropes.
#   Then dp[n][L] = min(dp[n-1][L], min_{a <= t <= b} dp[n-1][t] + p)
# Time complexity: O(N * L^2)
#
# Reduce the time complexity to O(N * L) by
#   using dequeue to maintain the minimum value of dp[n-1][t] + p for t in [L-b, L-a].
#   or more general (but complex): segment table, or sparse table, etc.
# Note: the reason we can use a dequeue is that the minimum query is a simple sliding window:
#   the window is [L-b, L-a], and when L increases by 1, the window moves right by 1.

from dataclasses import dataclass
from math import inf
from typing import List
from collections import deque

@dataclass
class ProblemData:
    N: int  # Number of ropes
    M: int  # Maximum money available
    L: int  # Target length to reach or exceed
    A: List[int]  # Minimum length of each rope
    B: List[int]  # Maximum length of each rope
    P: List[int]  # Cost of each rope


class SlidingWindowMin:
    def __init__(self, values):
        self.values = values
        self.dq = deque()

    def add(self, idx):
        if idx >= 0:
            val = self.values[idx]
            while self.dq and self.values[self.dq[-1]] >= val:
                self.dq.pop()
            self.dq.append(idx)

    def remove_before(self, min_idx):
        if self.dq and self.dq[0] < min_idx:
            self.dq.popleft()

    def get_min(self):
        return self.values[self.dq[0]] if self.dq else inf


def solve(data: ProblemData):
    # dp[l] = min cost to reach a range [S_A, S_B] that covers length l
    dp = [inf] * (data.L + 1)
    dp[0] = 0

    for n in range(data.N):
        a, b, p = data.A[n], data.B[n], data.P[n]
        new_dp = list(dp)  # Copy for not picking the rope

        # Sliding window minimum for picking the rope
        # We need min(dp[t]) for t in [l-b, l-a]
        sw = SlidingWindowMin(dp)
        for l in range(data.L + 1):
            sw.add(l - a)
            sw.remove_before(l - b)

            min_prev_cost = sw.get_min()
            if min_prev_cost != inf:
                new_dp[l] = min(new_dp[l], min_prev_cost + p)

        dp = new_dp

    return dp[data.L]


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

    data = ProblemData(N, M, L, A, B, P)
    ans = solve(data)

    print('Case #%d: %s' % (t, str(ans) if ans <= data.M else 'IMPOSSIBLE'))
