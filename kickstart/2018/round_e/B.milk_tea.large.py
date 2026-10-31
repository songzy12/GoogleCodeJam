T = int(input())

from heapq import heappush, heappop


def solve(p, f, P):
    origin = ['' for i in range(P)]

    cost = []

    def compute_cost(i):
        cnt0 = cnt1 = 0
        for a in p:
            if (int(a, 2) & (1 << (P - 1 - i))) ^ (1 << (P - 1 - i)):
                cnt0 += 1
            else:
                cnt1 += 1

        if cnt0 > cnt1:
            origin[i] = '0'
            return cnt0 - cnt1
        else:
            origin[i] = '1'
        return cnt1 - cnt0

    def compute(case, p):
        temp = 0
        p = list(map(lambda x: int(x, 2), p))
        case = int(''.join(case), 2)
        for a in p:
            temp += sum(map(int, bin(a ^ case)[2:]))
        return temp

    for i in range(P):
        cost.append([compute_cost(i), i, origin[i]])

    # print(origin)
    # print(cost)

    heap = [[0, origin]]
    visited = {''.join(origin)}

    while heap:
        cur_cost, cur_config = heappop(heap)
        # print(''.join(cur_config))
        if ''.join(cur_config) not in f:
            return compute(''.join(cur_config), p)
        for c, index, char in cost:
            next_config = cur_config[:index] + ['1' if char == '0' else '0'] + cur_config[index + 1:]
            if ''.join(next_config) in visited:
                continue
            else:
                visited.add(''.join(next_config))
            heappush(heap, [cur_cost + c, next_config])


for t in range(1, T + 1):
    N, M, P = map(int, input().split())
    p = []
    for n in range(N):
        p.append(input())
    f = []
    for m in range(M):
        f.append(input())
    print("Case #%d: %d" % (t, solve(p, f, P)))
