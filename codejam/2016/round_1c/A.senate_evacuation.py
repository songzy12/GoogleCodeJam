T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    P = map(int, raw_input().split())
    count = [[chr(i + ord('A')), c] for i, c in enumerate(P)]
    def compute(count):
        res = []
        while sum([c for (i, c) in count]):
            def get_next(count):
                count = sorted(count, key=lambda x:x[1], reverse=True)
                if len(count) == 1:
                    i, c = count[0]
                    num = 2 if c > 1 else 1
                    count[0][1] -= num
                    return i * num
                i0, c0 = count[0]
                i1, c1 = count[1]
                if c0 - c1 > 0:
                    num = 2 if c0 > 1 else 1
                    count[0][1] -= num
                    return i0 * num
                else:
                    if c0 == 1 and len(count) > 2 and count[2][1] == 1:
                        count[0][1] -= 1
                        return i0
                    count[0][1] -= 1
                    count[1][1] -= 1
                    return i0+i1
            res += [get_next(count)]
        return res
    res = compute(count)
    print "Case #%d:" % t,
    for i in res:
        print i,
    print
            
        
    
    
        
        
        
    
    
