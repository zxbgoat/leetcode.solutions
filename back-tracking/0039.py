class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cdds = sorted(candidates)
        rsts = []
        
        def combine(rst, idx):
            if sum(rst) == target:
                rsts.append(rst)
                return
            for i in range(idx, len(cdds)):
                if sum(rst) + cdds[i] <= target:
                    combine(rst+[cdds[i]], i)
                else:
                    break
        
        combine([], 0)
        return rsts