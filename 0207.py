from sys import stdin

n = int(stdin.readline().strip())
adjmat = [[0 for _ in range(n)] for _ in range(n)]
for line in stdin.readlines():
    dts, src = list(map(int, line.strip().split()))
    adjmat[src][dst] = 1
