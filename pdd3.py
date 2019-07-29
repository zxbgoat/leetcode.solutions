from sys import stdin

N = int(stdin.readline().strip())
L = list(map(int, stdin.readline().strip().split()))
W = list(map(int, stdin.readline().strip().split()))
M = {}
for i in range(N):
    if L[i] not in M:
        M[L[i]] = [W[i]]
    else:
        M[L[i]].append(W[i])
L_ = sorted(M.keys())
L = [L_[N-1-i] for i in range(N)]
# print(L)

dp = [0 for _ in range(N)]
dp[0] = max(M[L[0]]) * 7
i = 1
while i < len(L):
    dp[i] = min(dp[i-1]-max(M[L[i]]), max(M[L[i]])*7)
    # print(dp)
    if dp[i] == 0:
        break
    i += 1
print(i+1)