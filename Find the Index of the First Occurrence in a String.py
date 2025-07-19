class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index1 = haystack.find(needle)
        return index1
    
#----------------------------------------------------
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack < needle:
            return -1
        
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1