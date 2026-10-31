T = int(input())

ways = 0
for t in range(1, T+1):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    
    def solve(N):
        length = []
        visited = {}
        global ways
        ways = 0
        
        def dfs(i, N, length):
            # we are checking row i
            if i == N:
                def deal_with(length):                    
                    if len(length) < 3:
                        return
                    # print('dfs: ', length)

                    _used = [0 for i in range(len(length))]
                    def dfs_(i):
                        if i == len(length):
                            def check(_used):
                                combination = tuple([length[t][-1] for t in range(len(_used)) if _used[t]])
                                if combination in visited:
                                    return False
                                visited[combination] = True
                                length_ = [length[t][0] for t in range(len(_used)) if _used[t]]
                                if len(length_) < 3:
                                    return False
                                #print('combination', combination)
                                #print('length_:', length_)
                                return 2 * max(length_) < sum(length_)
                                
                            if check(_used):
                                global ways
                                ways += 1
                            return;
                        dfs_(i+1)
                        
                        _used[i] = 1
                        dfs_(i+1)
                        _used[i] = 0

                    dfs_(0)
                
                deal_with(length)
                return 

            for j in range(i + 1, N):
                if (graph[i][j]):
                    temp = {(i, j): graph[i][j]}

                    graph[i][j] = graph[j][i] = 0
                    for c in range(N):
                        if graph[i][c]:
                            temp[(i, c)] = graph[i][c]
                            graph[i][c] = graph[c][i] = 0
                    for r in range(N):
                        if graph[r][j]:
                            temp[(r,j)] = graph[r][j]
                            graph[r][j] = graph[j][r] = 0

                 
                    dfs(i + 1, N, length + [(temp[(i,j)], (i, j))])

                    for r, c in temp:
                        graph[r][c] = temp[(r,c)]
                        graph[c][r] = temp[(r,c)]
                  
            dfs(i + 1, N, length)

        dfs(0, N, length)
        return ways
            

    print("Case #%d: %d" %(t, solve(N)))
