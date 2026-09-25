# https://zibada.guru/gcj/ks2016a/problems/#B
#
# https://leetcode.com/problems/trapping-rain-water-ii/,

from sys import stdin

MAX_HEIGHT = 1005


def compute(H, R, C):
    ans = 0
    # First, imagine the water at each cell is so high.
    W = [[MAX_HEIGHT for j in range(C)] for i in range(R)]

    active_cell = []
    for i in range(R):
        W[i][0] = H[i][0]
        W[i][C-1] = H[i][C-1]
        active_cell += (i, 0),
        active_cell += (i, C-1),
    for j in range(C):
        W[0][j] = H[0][j]
        W[R-1][j] = H[R-1][j]
        active_cell += (0, j),
        active_cell += (R-1, j),

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while active_cell:
        # NOTE: if we use heap to select the lowerest active cell, 
        # then it will be just like solution 1. 
        r, c = active_cell.pop(0)
        for d in directions:
            rr = r + d[0]
            cc = c + d[1]
            if rr < 0 or rr == R or cc < 0 or cc == C:
                continue

            # Then, see whether the water at cell (rr, cc) would be flowed elsewhere
            # due to the active cell lower than its current water height.
            w_upperbound = max(H[rr][cc], W[r][c])
            if w_upperbound < W[rr][cc]:
                W[rr][cc] = w_upperbound
                active_cell += (rr, cc),

    for i in range(R):
        for j in range(C):
            ans += W[i][j] - H[i][j]
    return ans


T = int(input())
for t in range(T):
    R, C = map(int, stdin.readline().strip().split())
    H = []
    for i in range(R):
        H += list(map(int, stdin.readline().strip().split())),

    ans = compute(H, R, C)

    print(f"Case #{t+1}: {ans}")
