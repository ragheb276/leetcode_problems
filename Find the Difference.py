class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for c in t:
            count[c] = count.get(c, 0) + 1
        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]

        return list(count.keys())[0]
    
    
#----------------------------------------------
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
       for c in t:
           if t.count(c) > s.count(c):
               return c 
 