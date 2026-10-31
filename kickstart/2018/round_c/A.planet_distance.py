from collections import defaultdict
from copy import deepcopy

T = int(input())

def solve(edges, degree, N):
    # index from 1 to N
    # one circle

    not_in = set()

    edges_bak = deepcopy(edges)
    current = []
    for i in range(1, N + 1):
        if degree[i] == 1:
            current.append(i)
    while current:
        node = current.pop(0)
        not_in.add(node)
        for v in edges[node]:
            degree[v] -= 1
            degree[node] -= 1
            edges[v].remove(node)
            edges[node].remove(v)
            if degree[v] == 1:
                current.append(v)

    # now not_in is the one not in circle
    distance = {}
    for i in range(1, N + 1):
        if i in not_in:
            continue
        distance[i] = 0

    # now we construct a new graph
    # the nodes in circle would be node 0
    edges = edges_bak
    edges_new = defaultdict(list)
    for i in edges:
        for j in edges[i]:
            temp_i = i if i in not_in else 0
            temp_j = j if j in not_in else 0
            edges_new[temp_i].append(temp_j)

    # now edges_new is the new graph
    queue = [0]
    visited = set([0])
    distance[0] = 0
    while queue:
        node = queue.pop(0)
        for next_node in edges_new[node]:
            if next_node in visited:
                continue
            distance[next_node] = distance[node] + 1
            queue.append(next_node)
            visited.add(next_node)

    return [distance[i] for i in range(1, N+1)]

for t in range(1, T+1):
    N = int(input())
    degree = defaultdict(int)
    edges = defaultdict(list)
    for n in range(N):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)
        degree[x] += 1
        degree[y] += 1
    print("Case #%d: %s" %(t, ' '.join(map(str, solve(edges, degree, N)))))
        
