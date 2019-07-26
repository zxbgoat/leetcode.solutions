class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        rsts = []
        
        def perm(rst):
            if len(rst) == len(nums):
                rsts.append(rst)
                return
            for num in nums:
                if num not in rst:
                    perm(rst+[num])
        
        perm([])
        return rsts