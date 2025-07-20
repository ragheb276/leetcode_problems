class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1

        i = 0
        while i < len(t):
            c = t[i]
            if c in count_s:
                count_s[c] -= 1
                if count_s[c] == 0:
                    del count_s[c]
            else:
                return False
            i += 1

        if not count_s:
            return True
        else:
            return False

#-----------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            count[c] = count.get(c, 0) - 1

        for val in count.values():
            if val != 0:
                return False

        return True
#------------------------------------------------
