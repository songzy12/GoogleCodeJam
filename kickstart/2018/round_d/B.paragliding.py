# as long as h - p >= y - x and x <= p
# or (x >= p) and h + p >= y + x
# compute all h - p
# compute all y - x


def solve(K, N, x, y, p, h):

    x_y = []
    for i in range(K):
        x_y.append([x[i], y[i]-x[i], y[i]])
    x_y.sort()
    p_h = sorted(zip(p, [h[i] - p[i] for i in range(N)]))

    from heapq import heappush

    cnt = 0

    heap = []
    next_x = []

    j = N - 1
    for i in range(K - 1, -1, -1):
        while j >= 0 and p_h[j][0] >= x_y[i][0]:
            heappush(heap, -p_h[j][1])
            j -= 1
        if heap and x_y[i][1] <= -heap[0]:
            cnt += 1
        else:
            next_x += [[x_y[i][0], x_y[i][0] + x_y[i][-1]]]

    p_h = sorted(zip(p, [h[i] + p[i] for i in range(N)]))
    j = 0
    heap = []

    next_x.sort()

    for i in range(len(next_x)):
        while j < N and p_h[j][0] < next_x[i][0]:
            heappush(heap, -p_h[j][1])
            j += 1

        if heap and next_x[i][1] <= -heap[0]:
            cnt += 1

    return cnt

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    p1, p2, a1, b1, c1, m1 = map(int, input().split())
    h1, h2, a2, b2, c2, m2 = map(int, input().split())
    x1, x2, a3, b3, c3, m3 = map(int, input().split())
    y1, y2, a4, b4, c4, m4 = map(int, input().split())

    p = []
    h = []
    x = []
    y = []

    for i in range(N):
        p.append(p1)
        temp = ((a1 * p2 + b1 * p1 + c1) % m1) + 1
        p1 = p2
        p2 = temp
    for i in range(N):
        h.append(h1)
        temp = ((a2 * h2 + b2 * h1 + c2) % m2) + 1
        h1 = h2
        h2 = temp
    for i in range(K):
        x.append(x1)
        temp = ((a3 * x2 + b3 * x1 + c3) % m3) + 1
        x1 = x2
        x2 = temp
    for i in range(K):
        y.append(y1)
        temp = ((a4 * y2 + b4 * y1 + c4) % m4) + 1
        y1 = y2
        y2 = temp

    print("Case #%d: %d" % (t, solve(K, N, x, y, p, h)))
