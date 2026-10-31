# -*- coding: cp936 -*-
# A star can match between zero and four letters
# 因为*代表0个或者最多4个字符，将*展开成 ****，每个*匹配0个或者1个字符

def solve(p0, p1):
    
##    p0 = p0.replace('*', '*'*4)
##    p1 = p1.replace('*', '*'*4)
##    m = {}
##    def dp(i, j):
##        # index i of p0, index j of p1,
##        # leading * can match k chars (k = -4,...,4)
##        if (i, j) in m:
##            return m[(i,j)]
##        if i == len(p0):
##            m[(i,j)] = not p1[j:].replace('*', '')
##            return m[(i,j)]
##        if j == len(p1):
##            m[(i,j)] = not p0[i:].replace('*', '')
##            return m[(i,j)]
##
##        # i != len(p0) and j != len(p1)
##        if p0[i] == '*' and p1[j] != '*':
##            m[(i,j)] = dp(i+1, j) or dp(i+1, j+1)
##        elif p1[j] == '*' and p0[i] != '*':
##            m[(i,j)] = dp(i, j+1) or dp(i+1, j+1)
##        elif p0[i] != '*' and p1[j] != '*':
##            m[(i,j)] = (p0[i] == p1[j]) and dp(i+1, j+1)
##        else:
##            m[(i,j)] = dp(i, j+1) or dp(i+1, j+1) or dp(i+1, j)
##        return m[(i,j)]    
##    return dp(0, 0)

T = int(raw_input())
for t in range(T):
    p0 = raw_input()
    p1 = raw_input()
    print "Case #%d: %s" % (t+1, "TRUE" if solve(p0, p1) else "FALSE")
