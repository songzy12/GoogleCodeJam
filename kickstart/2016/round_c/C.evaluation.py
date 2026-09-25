# https://zibada.guru/gcj/ks2016c/problems/#C
#
# Topological sort.

from collections import defaultdict


def check_exps(exps):
    m = defaultdict(list)
    count = defaultdict(int)
    for exp in exps:
        v, r = exp.split('=')
        l = r.split('(')[-1].split(')')[0].split(',')
        # v do not depend on anything.
        if not l or not l[0]:
            count[v] = 0
            continue
        count[v] += len(l)
        for x in l:
            m[x].append(v)

    while 0 in count.values():
        for key, value in list(count.items()):
            if value == 0:
                for x in m[key]:
                    count[x] -= 1
                count.pop(key)
    return len(count) == 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    exps = []
    for n in range(N):
        exps.append(input())

    valid = check_exps(exps)
    print('Case #%d: %s' % (t, 'GOOD' if valid else 'BAD'))
