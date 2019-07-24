class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.rsts = []
        if not digits:
            return self.rsts
        d2c = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        """
        def combine(digits, rst):
            if not digits:
                self.rsts.append(rst)
                return
            digit = digits[0]
            for char in d2c[digit]:
                combine(digits[1:], rst+char)
        combine(digits, '')
        return self.rsts
        """
        rsts = ['']
        for i in digits:
            rsts = [x+y for x in rsts for y in d2c[i]]
        return rsts