class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        i, n, ms, s = 0, len(nums), 0, 0
        while i < n and nums[i] < 0:
            i += 1
        if i >= n:
            return max(nums)
        j = i
        while i < n and j < n:
            s += nums[j]
            if ms < s:
                ms = s
            if s < 0:
                i = j + 1
                j = i
                s = 0
                continue
            j += 1
        return ms