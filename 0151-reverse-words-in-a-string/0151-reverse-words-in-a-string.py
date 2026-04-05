class Solution:
    def reverseWords(self, s: str) -> str:
       res_l = s.split(" ")
       res_l.reverse()
       s = ""
       for elem in res_l:
        if elem != "":
            s += elem + " "
       return s.strip()