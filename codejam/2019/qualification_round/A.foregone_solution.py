T = int(input())

def solve(N):
    A = ""
    B = ""
    for t in N[::-1]:
        if t != '4':
            A = t + A
            B = '0' + B
        else:
            A = '1' + A
            B = '3' + B
    B = B.lstrip('0')
    return A + " " + B

for t in range(1, T+1):
    N = input()
    print("Case #%d: %s" % (t, solve(N)))
