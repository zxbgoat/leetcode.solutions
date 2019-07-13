import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()


def isMatch(s, p):
    m, n = len(s), len(p)
    mem = {}

    def dp(i, j):
        if (i, j) not in mem:
            if j == n:
                ans = i == m
            else:
                firstmatch = i < m and p[j] in {s[i], '.'}
                if j+1 < n and p[j+1] == '*':
                    ans = dp(i, j+2) or firstmatch and dp(i+1, j)
                else:
                    ans = firstmatch and dp(i+1, j+1)
            dp[i, j] = ans
        return dp[i, j]

    return dp(0, 0)


print(isMatch(s, p))
