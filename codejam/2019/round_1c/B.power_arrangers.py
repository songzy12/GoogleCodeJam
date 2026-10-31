# 119 + 23 + 5 + 1 < 150
import sys
from collections import defaultdict


def get_index(group, index):
    return 5 * group + index + 1

def _print(s):
    print(s)
    sys.stdout.flush()


T, F = map(int, input().split())
for t in range(1, T + 1):

    res = ''
    next_group = range(119)

    cnt = defaultdict(int)
    group = defaultdict(list)
    for i in next_group:
        index = get_index(i, 0)
        _print(index)
        c = input()
        cnt[c] += 1
        group[c].append(i)

    for c in 'ABCDE':
        if cnt.get(c, 0) == 23:
            next_group = group[c]
            res += c
            break

    cnt = defaultdict(int)
    group = defaultdict(list)
    for i in next_group:
        index = get_index(i, 1)
        _print(index)
        c = input()
        cnt[c] += 1
        group[c].append(i)

    for c in 'ABCDE':
        if cnt.get(c, 0) == 5:
            next_group = group[c]
            res += c
            break

    cnt = defaultdict(int)
    group = defaultdict(list)
    for i in next_group:
        index = get_index(i, 2)
        _print(index)
        c = input()
        cnt[c] += 1
        group[c].append(i)

    for c in 'ABCDE':
        if cnt.get(c, 0) == 1:
            next_group = group[c]
            res += c
            break

    cnt = defaultdict(int)
    group = defaultdict(list)
    for i in next_group:
        index = get_index(i, 3)
        _print(index)
        c = input()
        cnt[c] += 1
        group[c].append(i)

    for c in 'ABCDE':
        if cnt.get(c, 0) == 0:
            continue
        for _c in 'ABCDE':
            if _c not in res and _c != c:
                res = res + _c + c
                break
    
    _print(res)
    verdict = input()
    if verdict == 'Y':
        continue
    else:
        exit()

# python3 interactive_runner.py python3 testing_tool.py 0 -- python3 "Power Arrangers.py"