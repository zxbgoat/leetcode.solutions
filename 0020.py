class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in maps:
                top = stack.pop() if stack else '*'
                if top != maps[c]:
                    return False
            else:
                stack.append(c)
        return not stack