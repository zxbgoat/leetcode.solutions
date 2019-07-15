from sys import stdin

s = stdin.readline().strip()
p = stdin.readline().strip()


def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    # dp[i][j]表示s[:i+1]与p[:j+1]是否匹配
    dp = [[False for j in range(n+1)] for i in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] != '*':
                dp[i][j] = p[j-1] in {s[i-1], '?'} and dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
    return dp[-1][-1]


print(isMatch(s, p))
