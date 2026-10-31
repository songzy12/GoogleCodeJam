# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
# https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/

# https://www.cs.colorado.edu/~srirams/courses/csci2824-spr14/pollardsRho.html

# there is no need to use Pollard's Rho Algorithm
# we can just compute the gcd of the first and second number,
# that will give us the second prime number


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def solve(A, L):
    P = [None for i in range(L + 1)]
    i = 0
    while A[i] == A[i + 1]:
        i += 1

    # 0, ..., i, i+1, ...
    P[i + 1] = gcd(A[i], A[i + 1])

    for j in range(i, -1, -1):
        P[j] = A[j] // P[j + 1]

    for j in range(i + 1, L):
        P[j + 1] = A[j] // P[j]

    # print(A)
    # print(P)

    primes = sorted(set(P))
    import string
    chars = string.ascii_uppercase

    # print(primes)
    # print(chars)

    m = {}
    for i in range(len(primes)):
        m[primes[i]] = chars[i]

    # print(m)

    return ''.join([m[x] for x in P])

T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    A = map(int, input().split())
    print("Case #%d: %s" % (t, solve(list(A), L)))
