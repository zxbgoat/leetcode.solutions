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
N = len(L_)
L = [L_[N-1-i] for i in range(N)]

wp = [0 for _ in range(N)]
fp = [0 for _ in range(N)]
wp[0] = max(M[L[0]]) * 7
fp[0] = 1
i = 1
while i < N:
    ws = sorted(M[L[i]])
    flag = False
    for w in ws:
        if w * 7 > wp[i-1]:
            wp[i] = wp[i-1] + w
            fp[i] = fp[i-1] + 1
            flag = True
            break
    if not flag:
        wp[i] = wp[i-1]
        fp[i] = fp[i-1]
    i += 1
print(fp[i-1])