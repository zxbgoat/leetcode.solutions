import sys


def longestPalindrome(s: str) -> str:
    sz = len(s)
    if sz <= 1:
        return s
    dp = [[False for _ in range(sz)] for _ in range(sz)]
    longest = 1
    res = s[0]
    for r in range(1, sz):
        for l in range(r):
            if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                dp[l][r] = True
                curlen = r - l + 1
                if longest < curlen:
                    longest = curlen
                    res = s[l: r+1]
    return res
