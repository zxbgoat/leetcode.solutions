from pprint import pprint
from sys import stdin


def minDistance_topdn(word1: str, word2: str) -> int:
    # dp[i][j]表示word1[:i]与word2[:j]之间的编辑距离
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    return dp[-1][-1]


def minDistance_btmup(word1: str, word2: str) -> int:
    # dp[i][j]表示word1[:i]与word2[:j]之间的编辑距离
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m-1, -1, -1):
        dp[i][n] = m - i
    for j in range(n-1, -1, -1):
        dp[m][j] = n - j
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1


word1 = stdin.readline().strip()
word2 = stdin.readline().strip()
print(minDistance_topdn(word1, word2))
print(minDistance_btmup(word1, word2))
