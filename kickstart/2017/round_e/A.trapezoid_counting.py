# somtimes brute force sego.
# the parameter range is not large

def solve(s):
    dp = {}
    def get_dp(i, buf):
        if i == len(s):
            return 0
        if (i, buf) in dp:
            return dp[i, buf]
        
        res = 1 + get_dp(i+1, buf) # one char

        if buf and s[i:].startswith(buf):
            # res = min(res, 1 + get_dp(i + len(buf), buf)) # paste
            res = 1 + get_dp(i + len(buf), buf)

        for l in range(1, len(s[i:])+1):
            if s[i:i+l] in s[:i]:
                res = min(res, 2 + get_dp(i+l, s[i:i+l]))
                
        dp[i, buf] = res
        return dp[i, buf]
        
    return get_dp(0, '')

##s = 'rlgligrriirlgligrriirliligrriirlgligrriirlgligrriirlgligrriirlgligrriirlgligrriirlgligrriirlgligrrii'
##print solve(s)

T = int(raw_input())
for t in range(1, T+1):
    s = raw_input()
    print 'Case #%d: %d' % (t, solve(s))
