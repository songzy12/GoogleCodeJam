# 边长为k的平行于坐标轴的格点正方形，它正好是k个正方形的最小外接正方形

p = 1000000007
T = int(raw_input())

def sum1(N):
    # return \sum_{i=1}^N i
    return N*(N+1)/2 

def sum2(N):
    # return \sum_{i=1}^N i^2
    return N*(N+1)*(2*N+1)/6 

def sum3(N):
    # return \sum_{i=1}^N i^3
    return sum1(N)*sum1(N) 

def solve(R, C):
    ans = R*R*C-(R+C)*sum1(R-1)+sum2(R-1)+R*C*sum1(R-1)-(R+C)*sum2(R-1)+sum3(R-1)
    return ans % p

# R rows and C columns of dots, thus R-1 rows and C-1 columns of squares
for t in range(T):
    R, C = map(int, raw_input().split())
    if R > C:
        R, C = C, R
    print "Case #%d: %d" % (t + 1, solve(R-1, C-1))

# suppose R < C

# for parallel squares, the side length can be from 1 to R
# for square with side length l, the number is (R-l+1)*(C-l+1)

# for lopsided squares, the side length can be decided by a left point and a top point.
# for left point i and top point j,
# we have the bottom point at row i+j, right point at column i+j
# thus we need i+j < R, and the number is (R-(i+j)+1)*(C-(i+j)+1)
# for i+j = t, the number of different i and j is just t-1

# so sum them up, we have
#   \sum_{l=1}^{R} (R-l+1)*(C-l+1) + \sum_{t=1}^{R} (t-1)*(R-t+1)*(C-t+1)
# = \sum_{l=0}^{R-1} (R-l)*(C-l) + \sum_{t=0}^{R-1} t*(R-t)*(C-t)
# = RRC - (R+C) sum1(R-1) + sum2(R-1) + RC sum1(R-1) - (R+C) sum2(R-1) + sum3(R-1)
