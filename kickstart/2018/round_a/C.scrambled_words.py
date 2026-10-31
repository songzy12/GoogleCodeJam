# https://code.google.com/codejam/contest/9234486/dashboard#s=p2
T = int(input())

import string
from collections import defaultdict

for t in range(1, T+1):
    L = int(input())
    words = input().strip().split()
    S1, S2, N, A, B, C, D = input().strip().split()
    
    N, A, B, C, D = map(int, [N, A, B, C, D])

    #print(N, A, B, C, D)
    
    def generate(S1, S2, A, B, C, D):
        x = [ord(S1), ord(S2)]
        s = [S1, S2]
        
        for n in range(2, N):
            x.append((A * x[-1] + B * x[-2] + C) % D)
            s.append(chr(x[-1] % 26 + 97))
        return ''.join(s)
    s = generate(S1, S2, A, B, C, D)
    # print(len(s), s)
    
    # L is 20000
    # for each of L, check whether it appears
    # N is at most 1000000

    # def convert(word):
    #   return tuple([word[0], word[-1]] + [word.count(x) for x in string.ascii_lowercase])

    start = defaultdict(list)
    char_cnt = [[0 for i in range(26)] for j in range(N+1)]

    for i, x in enumerate(s):
        start[x].append(i)
        for c in string.ascii_lowercase:
            char_cnt[i+1][ord(c)-ord('a')] = char_cnt[i][ord(c) - ord('a')] + (1 if c == x else 0)
                
    def char_count(left, right):
        return tuple([char_cnt[right][ord(x)-ord('a')]-char_cnt[left][ord(x)-ord('a')] for x in string.ascii_lowercase])

    def char_count(left, right, goal):
        for x in string.ascii_lowercase:
            if char_cnt[right][ord(x)-ord('a')]-char_cnt[left][ord(x)-ord('a')] != goal[ord(x)-ord('a')]:
                return False
        return True
            
    def check(word):
        n = len(word)
        goal = tuple([word.count(x) for x in string.ascii_lowercase])
        # print(word, goal)
        for left in start[word[0]]:
            right = left + n
            # print(left, right, char_count(left, right))
            if right > N: # NOTE: index
                return False
            if s[right - 1] != word[-1]:
                continue
            if char_count(left, right, goal):
                return True
        return False
    
    cnt = 0
    for word in words:
        if check(word):
            cnt += 1
    print("Case #%d: %d" % (t, cnt))

    
    
    
