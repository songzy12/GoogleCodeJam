T = int(input())

def solve(s):
    r = ''
    for t in s:
        if t == 'E':
            r += 'S'
        else:
            r += 'E'
    return r
    
for t in range(1, T+1):
    N = int(input())
    s = input()
    print("Case #%d: %s" % (t, solve(s)))