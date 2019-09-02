from sys import stdin

n, m, k = list(map(int, stdin.readline().strip().split()))

numat = [[i*j for i in range(1, m+1)] for j in range(1, n+1)]
s, i = 0, 0
while s <= k:
    i += 1
    s += i
s -= i
