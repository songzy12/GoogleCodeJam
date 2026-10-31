import math

T = int(input())


def compute_group(N):
    # first compute which group, i.e., how many times each letter repeats.
    # 1st group has 26, 2nd group has 26*2
    # a_1 = 26, a_2 = 26(1+2), a_n = 26(1+...+n)=13n(n+1)
    # let n be the first one that N <= 13n(n+1)
    # 13(n-1)n < N <= 13n(n+1)
    # 13(n-1)^2 < N < 13(n+1)^2
    # (N/13)^0.5 -1 < n < (N/13)^0.5 + 1
    temp = math.floor((N / 13)**0.5 - 1)
    for t in range(temp, temp + 5):
        if 13 * t * (t + 1) >= N:
            return t


def compute(N):
    n = compute_group(N)
    N -= 13 * (n - 1) * n
    if N % n == 0:
        return chr(ord('A') - 1 + N // n)
    else:
        return chr(ord('A') + N // n)


for t in range(T):
    N = int(input())
    print(f"Case #{t+1}: {compute(N)}")
