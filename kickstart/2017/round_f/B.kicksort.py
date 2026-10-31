T = int(raw_input())
from collections import deque
for t in range(1, T+1):
    E, N = map(int, raw_input().split())
    
    S = map(int, raw_input().split())
    S.sort()
    S = deque(S)
    
    honor = 0
    
    while len(S):
        if E > S[0]:
            honor += 1
            E -= S[0]
            S.popleft()
        else:
            if len(S) > 1 and honor > 0:
                honor -= 1
                E += S[-1]
                S.pop()
            else:
                break
    print "Case #%d: %d" % (t, honor)
    
