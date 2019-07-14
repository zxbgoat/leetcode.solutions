from sys import stdin

s = stdin.readline().strip()
p = stdin.readline().strip()


def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False for j in range(n+1)] for i in range(m+1)]
    dp[-1][-1] = True
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if p[j] != '*':
                dp[i][j] = p[j] in {s[i], '?'} and dp[i+1][j+1]
            else:
                dp[i][j] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j+1]
    return dp[0][0]


print(isMatch(s, p))
