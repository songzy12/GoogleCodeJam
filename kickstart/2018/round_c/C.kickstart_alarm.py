T = int(input())

for t in range(1, T+1):
    N, K, x1, y1, c, d, e1, e2, f = map(int, input().split())
    p = int(1e9+7)
    def solve():
        x = [x1]
        y = [y1]
        for n in range(N-1):
            next_x = (c*x[-1]+d*y[-1]+e1)%f
            next_y = (d*x[-1]+c*y[-1]+e2)%f
            x.append(next_x)
            y.append(next_y)
        a = [(x[i]+y[i])%f for i in range(N)]

        power = 0

        def compute(i, j, k):
            _power = 0
            for t in range(i, j+1):
                _power += a[t] * (t-i+1)**k
                _power %= p
            return _power

        for k in range(1, K+1):
            for i in range(N):
                for j in range(i, N):
                    power += compute(i, j, k)
                    power %= p
        return power
    
    print("Case #%d: %d" % (t, solve()))
