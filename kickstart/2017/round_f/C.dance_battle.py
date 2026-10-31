from numpy import linalg as LA
import numpy as np
import code

T = int(raw_input())

for t in range(1, T+1):
    N, M, P = map(int, raw_input().split())

    distance = np.matrix([[1<<31 for i in range(N)] for j in range(N)])
    
    for i in range(N):
        distance[i, i] = 0
    for m in range(M):
        u, v, d = map(int, raw_input().split())
        distance[u - 1, v - 1] = d
        distance[v - 1, u - 1] = d

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if distance[i, j] > distance[i, k] + distance[k, j]:
                    distance[i, j] = distance[i, k] + distance[k, j]

    distance = np.sum(distance, axis=0)
    
    p = np.array([0] * N)
    
    for i in range(P):
        p = (distance + np.sum(p) - p[0]) * 1. / (N - 1)
        
    print "Case #%d: %f" % (t, p[0,0])
