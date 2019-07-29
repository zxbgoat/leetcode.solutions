inf = float('inf')
distmat = [[0,1,12,inf,inf,inf],
           [inf,0,9,3,inf,inf],
           [inf,inf,0,inf,5,inf],
           [inf,inf,4,0,13,15],
           [inf,inf,inf,inf,0,4],
           [inf,inf,inf,inf,inf,0]]


def dijkstra(distmat, source):
    dist = distmat[source]
    num = len(dist)
    flag = [0 for i in range(num)]
    flag[source] = 1
    for i in range(num-1):
        min = inf
        for j in range(num):
            :q

