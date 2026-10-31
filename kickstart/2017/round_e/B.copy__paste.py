
def solve(nums):
    nums.sort()
    # for a, b, c, d. when need a == b, and |c - d| < 2 * a
    # then we enumerate possible a, fix c, and count d
    # consider the case a = b = c seperately
    

T = int(raw_input())
for t in range(1, T+1):
    n = int(raw_input())
    nums = map(int, raw_input().split())
    print 'Case #%d: %d' % (t, solve(nums))
