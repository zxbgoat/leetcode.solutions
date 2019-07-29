class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        rsts, n = [], len(nums)
        if not nums:
            return rsts
        cnt = 0
        for num in nums:
            if num == 0:
                cnt += 1
            if cnt >= 3:
                rsts.append([0,0,0])
                break
        for sep in range(n):
            if nums[sep] >= 0:
                break
        i = 0
        while i < sep:
            j = sep
            while j < n:
                if nums[i] + nums[j] > 0:
                    low, high = i+1, sep
                else:
                    low, high = sep, j
                for k in range(low, high):
                    if not nums[i] + nums[j] + nums[k]:
                        rsts.append([nums[i], nums[k], nums[j]])
                        break
                while j+1 < n and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            while i+1 < sep and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return rsts