T = int(input())

def plus(n):
    n = str(n)
    for i, t in enumerate(n):
        if t in '13579':
            break
    else:
        return 0
    
    if n[i] != '9':
        goal = str(int(n[:i+1])+1) + '0'*(len(n)-i-1)
        return int(goal) - int(n)
    
    # now n[i] == 0 and i != 0:
    goal = str(int(n[:i+1])+1) + '0' * (len(n)-i-1)
    
    return int(goal) - int(n) + plus(goal)
    
def minus(n):
    n = str(n)
    for i, t in enumerate(n):
        if t in '13579':
            break
    else:
        return 0
    
    goal = str(int(n[:i+1])-1) + '8'*(len(n)-i-1)
    return int(n) - int(goal)

def solve(n):
    if not minus(n):
        return plus(n)
    return min(minus(n), plus(n))

for t in range(1, T+1):
    N = int(input())
    print("Case #%d: %d" %(t, solve(N)))
