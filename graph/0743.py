class Solution:
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        inf = 1000
        
        def findmin(srcs, dsts):
            minval, minidx = inf, -1
            for i in range(N):
                if i not in srcs and dsts[i] < minval:
                    minval = dsts[i]
                    minidx = i
            return minidx, minval
        
        S = [K-1]
        # adjmat[i][j]表示从i到j所需时间
        adjmat = [[inf if i !=j else 0 for j in range(N)] for i in range(N)]
        for u, v, w in times:
            adjmat[u-1][v-1] = w
        dst = adjmat[K-1]
        for _ in range(N-1):
            minidx, mindst = findmin(S, dst)
            if mindst == inf:
                break
            S.append(minidx)
            for u in range(N):
                dst[u] = min(mindst+adjmat[minidx][u], dst[u])
        maxdst = max(dst)
        if maxdst == inf:
            return -1
        return maxdst