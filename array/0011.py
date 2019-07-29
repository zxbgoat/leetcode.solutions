class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        n, maxarea = len(height), 0
        """ 暴力法，超时
        for left in range(n-1):
            for right in range(left+1, n):
                # print(left, right)
                area = min(height[right], height[left]) * (right - left)
                if maxarea < area:
                    maxarea = area
        """
        
        # 双指针法
        left, right = 0, n-1
        while left <= right:
            maxarea = max(maxarea, min(height[right],height[left])*(right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maxarea