T = int(raw_input())
for t in range(1, T + 1):
    N = int(raw_input())
    F = map(int, raw_input().split())
    F = [x - 1 for x in F]

    # find all the cycles
    visited = [False for i in range(N)]
    m = {}
    for x in range(N):
        if visited[x]:
            continue
        visited[x] = True
        while not visited[F[x]]:
            visited[F[x]] = True
            x = F[x]
        if F[x] not in m:
            current = origin = F[x]
            size = 1
            flag = False
            while F[current] != origin:
                size += 1
                current = F[current]
                if F[current] in m:
                    flag = True
                    break
            if flag:
                continue
            current = origin = F[x]
            m[current] = size
            while F[current] != origin:
                current = F[current]
                m[current] = size
    
    # out_degree is all 1
    in_degree = [0 for i in range(N)]
    for node in F:
        # from 1,...,N to 0,...,N-1
        in_degree[node] += 1
        
    q = []
    for node, degree in enumerate(in_degree):
        if degree == 0:
            q += node,

    # q is possible chain head
    cand = {}
    for node in q:
        cur_len = 1
        while F[node] not in m:
            cur_len += 1
            node = F[node]
        if m[F[node]] > 2:
            continue
        cand[F[node]] = max(cur_len, cand.get(F[node], 0))

    ans = 0
    
    for i in m:
        if m[i] > 2:
            ans = max(m[i], ans)
    temp = 0
    for i in m:
        if m[i] == 2:
            temp += m[i] + cand.get(i,0) + cand.get(F[i], 0)
    temp /= 2
    ans = max(temp, ans)
    print "Case #%d: %d" % (t, ans)
        
