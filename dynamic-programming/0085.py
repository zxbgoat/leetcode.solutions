class Solution:
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        if not matrix:
            return maxarea
        m, n = len(matrix), len(matrix[0])
        # dp[i][j]表示，在第i行，到matrix[i][j]连续1的最大数目
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = (dp[i][j-1] if j else 0) + 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width*(i-k+1))
        return maxarea


class Solutions:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        if not matrix:
            return maxarea
        m, n = len(matrix), len(matrix[0])
        left = right = height = [0] * n
        for i in range(m):
            curleft, curright = 0, n
            for j in range(n):
                height[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curleft)
                else:
                    left[j], curleft = 0, j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j] === '1':
                    right[j] = min(right[j], curright)
                else:
                    right[j], curright = n, j
            for j in range(n):
                maxarea = max(maxarea, (right[j]-left[j])*height[j])
        return maxarea
