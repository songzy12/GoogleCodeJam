# https://zibada.guru/gcj/ks2016d/problems/#B

def compute(row, col):
    '''
    xox xox xox ...
    xxo xxo xxo ...
    oxx oxx oxx ...
    ... ... ... ...
    '''
    if row > col:
        row, col = col, row

    if row <= 2:
        return row * (col - col // 3)
    return row * col - row * col // 3


T = int(input())
for t in range(1, T+1):
    r, c = map(int, input().split())
    ans = compute(r, c)
    print('Case #%d: %d' % (t, ans))
