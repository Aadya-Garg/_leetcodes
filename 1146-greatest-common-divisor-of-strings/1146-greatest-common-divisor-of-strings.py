class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t = ""
        if str1 not in str2 and str2 not in str1:
            return t
        
        len1 = len(str1)
        len2 = len(str2)

        if (len1 >= len2):
            smaller = str2
            min_ = len2
        else:
            smaller = str1
            min_ = len1

        #now loop on length of t (reference is smaller string)
        for i in range(min_ - 1, -1, -1):
            ref = i + 1
            t = smaller[:ref]
            
            freq1 = len1 // ref
            freq2 = len2 // ref
            
            if (t * freq1 == str1 and t * freq2 == str2):
                return t
        return ""


        