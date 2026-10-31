from itertools import combinations

visited = set()

def all_combinations(l):
    # len(list) == 9
    res = []

    for a in combinations(l, 3):
        list_a = [x for x in l if x not in a]
        for b in combinations(list_a, 3):
            list_b = tuple([x for x in list_a if x not in b])
            res.append([a, b, list_b])
        visited.add(a)
    return res

def get(com, p1):
    res = []
    for item in com:
        temp = []
        for a in item:
            temp.append([p1[i] for i in a])
        res.append(temp)
    return res

def win(com, com2):
    cnt = 0
    for i in range(3):
        def win_(t1, t2):
            return sum(t1) > sum(t2)
        if win_(com[i], com2[i]):
            cnt += 1
    # print(com, com2, cnt)
    return cnt >= 2


def compute_prob(com, com_p1):
    cnt = 0
    for com2 in com_p1:
        if win(com, com2):
            cnt += 1
    return cnt

def compute(p1, p2):    
    com = all_combinations([i for i in range(9)])
    #print(len(com))
    com_p1 = get(com, p1)
    com_p2 = get(com, p2)
    #print(com_p1)
    #print(com_p2)
    res = None
    for com in com_p2:
        temp = compute_prob(com, com_p1)
        if res == None or temp > res:
            res = temp
    return res

T = int(input())
for t in range(1, T+1):
    N = int(input())
    p2 = list(map(int, input().split()))
    p1 = list(map(int, input().split()))
    print("Case #%d: %f" %(t, compute(p1, p2)))