T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    R = map(int, raw_input().split())
    B = map(int, raw_input().split())

    graph = [[0]*N for _ in range(N)]

    # populate the graph
    for u in range(N):
        for v in range(N):
            if u == v:
                continue
            graph[u][v] = min(R[u] ^ B[v], R[v] ^ B[u])

    # initialize the MST and the set X
    T = set();
    X = set();

    # select an arbitrary vertex to begin with
    X.add(0);

    while len(X) != N:
        crossing = set();
        # for each element x in X, add the edge (x, k) to crossing if
        # k is not in X
        for x in X:
            for k in range(N):
                if k not in X and graph[x][k] != 0:
                    crossing.add((x, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e:graph[e[0]][e[1]])[0];
        # add this edge to T
        T.add(edge)
        # add the new vertex to X
        X.add(edge[1])

    ans = 0
    # print the edges of the MST
    for u, v in T:
        ans += graph[u][v]
    print "Case #%d: %d" %(t, ans)
