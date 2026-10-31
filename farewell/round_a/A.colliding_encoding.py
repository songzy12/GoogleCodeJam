# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad7cf


def encode(s, m):
    res = ''
    for c in s:
        res += m[c]
    return res


T = int(input())
for t in range(T):
    D = list(input().split())
    m = {}
    for i in range(len(D)):
        m[chr(ord('A') + i)] = D[i]
    N = int(input())
    res = set()
    for n in range(N):
        s = input()
        res.add(encode(s, m))
    print(f"Case #{t+1}: ", "NO" if len(res) == N else "YES")
