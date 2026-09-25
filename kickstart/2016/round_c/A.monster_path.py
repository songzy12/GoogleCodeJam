# https://zibada.guru/gcj/ks2016c/problems/#A
#
# 1. dfs to enumerate all possible paths.
# 2. for a specific grid, if we have visited it n times, expected number of monster caught is 1-(1-p)**n

def compute_expectation(grid, count):
    res = 0
    for r in range(R):
        for c in range(C):
            res += 1 - (1 - grid[r][c]) ** count[r][c]
    return res


def solve(r, c, s, grid, count, ans):
    if s < 0:
        return ans
    if s == 0:
        res = compute_expectation(grid, count)
        return max(ans, res)

    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i, j in dirs:
        r_, c_ = r + i, c + j
        if r_ < 0 or r_ >= R or c_ < 0 or c_ >= C:
            continue

        count[r_][c_] += 1
        ans = solve(r_, c_, s - 1, grid, count, ans)
        count[r_][c_] -= 1
    return ans


T = int(input())
for t in range(1, T+1):
    R, C, R_s, C_s, S = map(int, input().split())
    P, Q = map(float, input().split())
    grid = []
    for r in range(R):
        grid.append(list(map(lambda x: P if x == 'A' else Q, input().split())))

    ans = 0
    count = [[0 for i in range(C)] for j in range(R)]
    ans = solve(R_s, C_s, S, grid, count, ans)
    print('Case #%d: %.9f' % (t, ans))
