class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        min_ = min(len1, len2)
        while i < min_:
            res += word1[i] + word2[i]
            i += 1
        
        if (len1 > len2):
            return res + word1[i:]
        
        if (len2 > len1):
            return res + word2[i:]
        
        return res
        
