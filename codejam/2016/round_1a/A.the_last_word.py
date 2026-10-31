T = int(raw_input())
for t in range(1, T+1):
    print "Case #%d:" % t,
    S = raw_input()
    ans = ""
    for i in S:
        if not ans:
            ans += i
        else:
            ans = i + ans if i >= ans[0] else ans + i
    print ans
    
