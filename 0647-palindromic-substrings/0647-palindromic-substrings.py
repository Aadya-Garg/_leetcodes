class Solution:
    def countSubstrings(self, s: str) -> int:
        reversed = s[::-1]
        len_ = len(s)
        temp = ""
        res = len_
        i = len_ - 1
        to_consider = ""
        #palindrom even numbers only after 3

        for i in range(len_ - 1):
            temp = s[i]
            for j in range(i+1, len_):
                temp += s[j]
                if temp == temp[::-1]:
                    res += 1
        return res
        
        