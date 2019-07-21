class Solution:
    
    def numTrees(self, n: int) -> int:
        # dp[i]表示长度为i的序列的二叉搜索树个数
        dp = [0 for _ in range(n+1)]
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, n+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]