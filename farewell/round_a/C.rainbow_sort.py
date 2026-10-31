T = int(input())


def compute(S):
    res = []
    res_set = set()
    for s in S:
        if s not in res_set:
            res_set.add(s)
            res.append(s)
        elif s == res[-1]:
            continue
        else:
            return False, []
    return True, res


for t in range(T):
    N = int(input())
    S = input().split()
    possible, res = compute(S)
    if not possible:
        print(f"Case #{t+1}: IMPOSSIBLE")
    else:
        print(f"Case #{t+1}:", *res)
