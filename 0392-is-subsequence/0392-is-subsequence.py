class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_t = len(t)
        for i in range(length_t - 1, -1, -1):
            if (s == ""):
                return True
            if (t[i] == s[-1]):
                s = s[:-1]
            
        return (s == "")
        