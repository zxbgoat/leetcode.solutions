# Time Linited Error
class Solution:
    
    def unique(self, s: str) -> bool:
        if len(s) == len(set(s)):
            return True
        return False
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.unique(s[i:j+1]):
                    l = max(l, j-i+1)
        return l


# Sliding window
class Solution:
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for i in range(len(s)):
            j = i + 1
            while j < len(s) and s[j] not in s[i:j]:
                j += 1
            l = max(l, j-i)
        return l


# Optimize the search
class Solution:
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, i = 0, 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] not in s[i:j]:
                    j += 1
            l = max(l, j-i)
            if j < len(s):
                i += s[i:j].index(s[j]) + 1
            else:
                i += 1
        return l