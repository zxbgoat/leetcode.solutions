class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.rsts = []
        
        def generate(S, left, right):
            if len(S) == 2*n:
                self.rsts.append(S)
                return
            if left < n:
                generate(S+'(', left+1, right)
            if right < left:
                generate(S+')', left, right+1)
        
        generate('', 0, 0)
        return self.rsts