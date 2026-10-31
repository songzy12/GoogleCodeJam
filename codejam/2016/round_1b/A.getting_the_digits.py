'''
digits = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
m = {}
for num, word in enumerate(digits):
    for char in word:
        m[char] = m.get(char, []) + [num]

for key in m:
    print key, set(m[key])
'''

T = int(raw_input())
for t in range(1, T+1):
    S = raw_input()
    # Z:0, W:2, U:4, X:6, G:8
    # H:3 8, F: 5 4, S: 7 6
    # O: 1 0 2 4, I: 9 5 6 8
    num = {}
    num[0] = S.count('Z')
    num[2] = S.count('W')
    num[4] = S.count('U')
    num[6] = S.count('X')
    num[8] = S.count('G')
    num[3] = S.count('H') - num[8]
    num[5] = S.count('F') - num[4]
    num[7] = S.count('S') - num[6]
    num[1] = S.count('O') - num[0] - num[2] - num[4]
    num[9] = S.count('I') - num[5] - num[6] - num[8]

    ans = ''
    for i in range(10):
        ans += str(i)*num[i]
    print 'Case #' + str(t) + ': ' + ans
    
