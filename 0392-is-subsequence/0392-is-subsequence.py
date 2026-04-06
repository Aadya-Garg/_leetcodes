class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_t = len(t)
        length_s = len(s)
        if length_s > length_t:
            return False
        if length_s == 0:
            return True
        char = s[0]
        s_ind = 0
        for i in range(length_t):
            if t[i] == char:
                if s_ind == length_s - 1:
                    return True
                s_ind += 1
                char = s[s_ind]
        return False
        # for i in range(length_t - 1, -1, -1):
        #     if (s == ""):
        #         return True
        #     if (t[i] == s[-1]):
        #         s = s[:-1]
            
        # return (s == "")
        