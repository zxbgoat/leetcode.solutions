class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


class Solution_On:

    def uniquePaths(self, m: int, n: int) -> int:
        rowpaths = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                rowpaths[j] += rowpaths[j-1]
        return rowpaths[-1]
