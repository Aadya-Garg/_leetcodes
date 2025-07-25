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
        return res + word1[i:] + word2[i:]
        
        
