T = int(input())
for t in range(1, T + 1):
    N, O, D = map(int, input().split())
    X1, X2, A, B, C, M, L = map(int, input().split())

    def solve(N, O, D, X1, X2, A, B, C, M, L):
        prefix = [0 for i in range(N + 1)]
        cnt_odd = [0 for i in range(N + 1)]

        for i in range(N):
            prefix[i + 1] = prefix[i] + X1 + L
            cnt_odd[i + 1] = cnt_odd[i] + ((X1 + L) % 2)
            temp = (A * X2 + B * X1 + C) % M
            X1 = X2
            X2 = temp

        def valid(head, tail):
            return cnt_odd[tail] - cnt_odd[head] <= O and \
                prefix[tail] - prefix[head] <= D

        ans = None
        tail = 0
        for head in range(N):
            while tail < N and valid(head, tail + 1):
                tail += 1
            if head >= tail or not valid(head, tail):
                continue
            temp = prefix[tail] - prefix[head]
            if not ans or temp > ans:
                ans = temp

        return str(ans) if ans != None else "IMPOSSIBLE"

    print("Case #%d: %s" % (t, solve(N, O, D, X1, X2, A, B, C, M, L)))

