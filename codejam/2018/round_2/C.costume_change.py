# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/0000000000045875

# 对于每个人，会影响到他的有 (N-1)*2 个人
# 而可选的颜色有 2*N 种

# 所以如果决定要改变一个人的颜色，
# 可以保证改完之后不影响其他所有人

# 给所有会影响的人连边
# 然后从度数最高的点开始删
# 直到图中没有边为止

# 咦这个和解析不太一样
# 我们来实现一下

# 恩这样确实是有问题的
# 因为我们不能确定如果 degree 一样
# 最先被 pop 出来的是哪一个

# 比如
# 0 0 x
# 0 x x
# x x 0

# 答案应该是 2 个

# 正确做法：二分图匹配

from collections import defaultdict
from heapq import heappush, heappop


def solve(grid):
    edges = defaultdict(set)
    degree = defaultdict(int)

    def add_edge(i1, j1, i2, j2):
        edges[(i1, j1)].add((i2, j2))
        edges[(i2, j2)].add((i1, j1))
        degree[(i1, j1)] += 1
        degree[(i2, j2)] += 1

    def compute():
        # print(edges)
        # print(degree)

        res = 0
        heap = []

        for k, v in degree.items():
            heappush(heap, (-v, k))
        while heap:
            v, k = heappop(heap)
            if degree[k] != -v:
                continue
            if degree[k] == 0:
                continue
            res += 1
            for node in edges[k]:
                degree[node] -= 1
                heappush(heap, (-degree[node], node))
                edges[node].remove(k)
        return res

    for i in range(len(grid)):
        for j1 in range(len(grid)):
            for j2 in range(j1 + 1, len(grid)):
                if grid[i][j1] == grid[i][j2]:
                    add_edge(i, j1, i, j2)
    for j in range(len(grid)):
        for i1 in range(len(grid)):
            for i2 in range(i1 + 1, len(grid)):
                if grid[i1][j] == grid[i2][j]:
                    add_edge(i1, j, i2, j)

    res = compute()
    return res


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(input().strip().split())
    # print(grid)
    print("Case #%d: %d" % (t, solve(grid)))
