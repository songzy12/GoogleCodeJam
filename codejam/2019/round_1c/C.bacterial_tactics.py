# -*- coding: utf-8 -*-

# 虽然在一步操作之后可以变成割裂的 subgrid ，
# 但是在这每一个 subgrid 中并不是一个 subgame，
# 因为双方在 subgrid 中的操作步数不一定相等


def solve(_grid, R, C):
    # . empty, # ,

    dp = {}

    def get_dp(grid, R, C):
        def check_safe(x, y, row):
            if grid[x * C + y] != '.':
                return ''
            temp = grid
            if row:
                t = y
                while t >= 0:
                    pos = x * C + t
                    if grid[pos] == '.':
                        temp = temp[:pos] + '*' + temp[pos + 1:]
                    elif grid[pos] == '*':
                        break
                    else:
                        return ''
                    t -= 1
                t = y
                while t < C:
                    pos = x * C + t
                    if grid[pos] == '.':
                        temp = temp[:pos] + '*' + temp[pos + 1:]
                    elif grid[pos] == '*':
                        break
                    else:
                        return ''
                    t += 1
            else:
                t = x
                while t >= 0:
                    pos = t * C + y
                    if grid[pos] == '.':
                        temp = temp[:pos] + '*' + temp[pos + 1:]
                    elif grid[pos] == '*':
                        break
                    else:
                        return ''
                    t -= 1
                t = x
                while t < R:
                    pos = t * C + y
                    if grid[pos] == '.':
                        temp = temp[:pos] + '*' + temp[pos + 1:]
                    elif grid[pos] == '*':
                        break
                    else:
                        return ''
                    t += 1
            return temp

        if grid in dp:
            return dp[grid]

        flag = 0
        for x in range(R):
            for y in range(C):
                next_grid = check_safe(x, y, 0)
                # print(next_grid, x, y, 0, grid)
                if next_grid:
                    if not get_dp(next_grid, R, C):
                        flag += 1
                next_grid = check_safe(x, y, 1)
                # print(next_grid, x, y, 0, grid)
                if next_grid:
                    if not get_dp(next_grid, R, C):
                        flag += 1
        dp[grid] = flag
        return flag

    return get_dp(_grid, R, C)


T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    grid = ""
    for _ in range(R):
        grid += input().strip()
    print("Case #%d: %d" % (t, solve(grid, R, C)))

# 首先就是函数的参数作用域的大坑！！

# 然后为啥重定向的时候 < 结果是错的 但是手敲就是对的呢
# WSL 的大坑！！
# 好吧不是因为 WSL 而是 Ubuntu 也这样，主要原因是没有加 .strip()
# 是 Windows 下换行符的原因