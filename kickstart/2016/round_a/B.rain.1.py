# https://zibada.guru/gcj/ks2016a/problems/#B
#
# This is avaliable on leetcode now: https://leetcode.com/problems/trapping-rain-water-ii/,
# which is a 2-dimensional generalization of the 1-dimension problem https://leetcode.com/problems/trapping-rain-water/
# A good explanation can be viewed here: https://leetcode.com/problems/trapping-rain-water-ii/solutions/89495/how-to-get-the-solution-to-2-d-trapping-rain-water-problem-from-1-d-case/

from multiprocessing import heap
from sys import stdin
import heapq


def compute(H, R, C):
    ans = 0

    boundary = []
    visited = set()
    # Add boundary cells as initial boundary.
    for r in range(R):
        heapq.heappush(boundary, (H[r][0], r, 0))
        heapq.heappush(boundary, (H[r][C-1], r, C-1))
        visited.add((r, 0))
        visited.add((r, C-1))
    for c in range(1, C-1):
        heapq.heappush(boundary, (H[0][c], 0, c))
        heapq.heappush(boundary, (H[R-1][c], R-1, c))
        visited.add((0, c))
        visited.add((R-1, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while boundary:
        # BFS from the lowest boundary cell.
        pool = [heapq.heappop(boundary)]
        while pool:
            h, r, c = pool.pop()
            for d in directions:
                rr = r + d[0]
                cc = c + d[1]
                if rr < 0 or rr == R or cc < 0 or cc == C:
                    continue

                if (rr, cc) in visited:
                    continue
                visited.add((rr, cc))

                if H[rr][cc] >= h:
                    # Add to boundary
                    heapq.heappush(boundary, (H[rr][cc], rr, cc))
                else:
                    # Add to pool
                    ans += h - H[rr][cc]
                    pool.append((h, rr, cc))

    return ans


T = int(input())
for t in range(T):
    R, C = map(int, stdin.readline().strip().split())
    H = []
    for i in range(R):
        H += list(map(int, stdin.readline().strip().split())),

    ans = compute(H, R, C)

    print(f"Case #{t+1}: {ans}")
