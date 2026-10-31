# 二分答案

# 问题在于：
# 并不是说：对于一个点，向它运动的人超过不向它运动的人
# 而是说：对于一个点，向它运动的人超过向其他点运动的人

# 计数的时候必须两个坐标一起考虑

T = int(input())


def solve(Q, dirs):
    # print(dirs)
    x0, y0 = 0, 0

    def check(x, y):
        cnt = 0
        for x0, y0, d0 in dirs:
            if d0 == 'N' and y > y0:
                cnt += 1
            if d0 == 'S' and y < y0:
                cnt += 1
            if d0 == 'W' and x < x0:
                cnt += 1
            if d0 == 'E' and x > x0:
                cnt += 1
        return cnt

    prev = check(x0, y0)

    for x, y, dir in sorted(dirs, key=lambda x: x[0]):
        cnt = check(x, y0)
        if cnt > prev:
            prev = cnt
            x0 = x

        if x < Q:
            cnt = check(x + 1, y0)
            if cnt > prev:
                prev = cnt
                x0 = x + 1

    prev = check(x0, y0)

    for x, y, dir in sorted(dirs, key=lambda x: x[1]):
        cnt = check(x0, y)
        # print(x0, y0, prev, x, y, cnt)
        
        if cnt > prev:
            prev = cnt
            y0 = y

        if y < Q:
            cnt = check(x0, y + 1)
            if cnt > prev:
                prev = cnt
                y0 = y + 1

    return str(x0) + " " + str(y0)


for t in range(1, T+1):
    P, Q = map(int, input().split())
    dirs = []
    for p in range(P):
        x, y, d = input().split()
        dirs.append([int(x), int(y), d])
    print("Case #%d: %s" % (t, solve(Q, dirs)))
