class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cdds = sorted(candidates)
        print(cdds)
        rsts = []
        
        def combine(rst, idx):
            print(rst, idx)
            if sum(rst) == target:
                rsts.append(rst)
                return
            i = idx
            while(i < len(cdds)):
                if sum(rst) + cdds[i] <= target:
                    combine(rst+[cdds[i]], i+1)
                    while i+1 < len(cdds) and cdds[i] == cdds[i+1]:
                        i += 1
                else:
                    break
                i += 1
        
        combine([], 0)
        return rsts