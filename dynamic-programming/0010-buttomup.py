import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False for _ in range(n+1)] for _ in range(m+1)]
    dp[-1][-1] = True
    for i in range(m, -1, -1):
        for j in range(n-1, -1, -1):
            firstmatch = i < m and p[j] in {s[i], '.'}
            if j+1 < n and p[j+1] == '*':
                dp[i][j] = dp[i][j+2] or firstmatch and dp[i+1][j]
            else:
                dp[i][j] = firstmatch and dp[i+1][j+1]
    return dp[0][0]


print(isMatch(s, p))
