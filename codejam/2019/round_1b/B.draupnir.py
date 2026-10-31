# encoding:utf8

# 类似斐波那契数列

# n1, n2, n3, n4, n5, n6
# 那么在第 d 天的时候，个数是
# n1*(1, 2, 3, 5, 8, 13, 21 )
# n2*(1, 0, 2, 2, 3, 0, 5, )
# n3*(1, 0, 0, 2, 0, 0, 3,)
# n4*(1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 8)
# n5*(1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5, 0)
# n6*(1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0)

# 2**63
# R_i <= 100
# 2**10 = 10**3
# 10**12 = 2**40

# 记斐波那契数列第 t 项为 F_t
# 1, 2, 3, 5

# 对于第 d 天，总数是 a_d
# n1 * F_d + n2 * F_{d//2} + ... + n6 * F_{d // 6}

# 希望找到这样的一个 d 在 1 到 500 之间
# 使得 F_d, F_{d//2}, ..., F_{d//6} 能够对于 6 个不同的素数的模线性无关
# 这样我们就能凑出六个式子了

# 先看看 d 从 1 到 500 都是些啥吧



try:
    input = raw_input
except NameError:
    pass

F = [1, 2]
while len(F) < 500 + 1:
    F.append(F[-1]+F[-2])

# 16 [2584, 55, 13, 8, 5, 3]

# 2584 * n1 + 55 * n2 + 13 * n3 + 8 * n4 + 5 * n5 + 3 * n6 = a_16

# 因为 n <= 100, 所以只要模大于100的素数就可以了


primes = [101, 103, 107, 109, 113, 127]

d = 500
n_500 = [(F[d//j] % 2**63) for j in range(1, 7)]
ans = [1, 0, 0, 0, 0, 0]

import numpy as np
from scipy.linalg import solve
import sys

T, W = map(int, input().split())
# T, W = 1, 1

for t in range(1, T+1):
    print(d)
    sys.stdout.flush()

    r = int(input())
    # r = sum([n_500[i]*ans[i] for i in range(6)])

    a = [[x % p for x in n_500] for p in primes]
    b = [r % p for p in primes]
    a = np.array(a)
    b = np.array(b)
    res = solve(a, b)
    # NOTE：这里有两个坑，一个是没有加 int，另一个是没有 " ".join()
    print(" ".join([str(int(x)) for x in res]))
    sys.stdout.flush()

    r = int(input())
    if r == -1:
        exit()

# NOTE: 好的，最大的大坑是这不是一个斐波那契数列，是一个指数数列
# NOTE：另一件事是我根本没搞明白这个 interactive 是怎么搞的
# python interactive_runner.py python testing_tool.py 0 -- python Draupnir.py
# python3 interactive_runner.py python3 testing_tool.py 0 -- python3 Draupnir.py

# 所以我终于知道是怎么回事了：
    # if r == -1:
    #     exit()

# 是的官方示例代码里没有出现 exit() 这个写法，大坑！