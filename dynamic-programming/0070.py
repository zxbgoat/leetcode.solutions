class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        stairs = [0 for _ in range(n)]
        stairs[0] = 1
        stairs[1] = 2
        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[-1]