# https://zibada.guru/gcj/ks2016a/problems/#C
#
# Newton's method: https://en.wikipedia.org/wiki/Newton%27s_method

from sys import stdin
from random import random

DELTA = 10**(-12)


def f(r, m, c):
    ans = 0
    ans += -c[0] * (1 + r)**m
    for i in range(1, m + 1):
        ans += c[i] * (1 + r)**(M - i)
    return ans


def df(r, m, c):
    ans = 0
    ans += -c[0] * m * (1 + r)**(m - 1)
    for i in range(1, m):
        ans += c[i] * (m - i) * (1 + r)**(m - i - 1)
    return ans


def it(x, m, c):
    return x - f(x, m, c) * 1.0 / df(x, m, c)


def compute(m, c):
    while True:
        x = random()
        xn = it(x, m, c)
        while abs(xn - x) > DELTA:
            x = xn
            xn = it(xn, m, c)
        if 1 > xn > -1:
            return xn


T = int(input())
for t in range(T):
    M = int(input())
    C = list(map(int, stdin.readline().strip().split()))

    x = compute(M, C)
    print(f"Case #{t+1}: {x:.12f}")
