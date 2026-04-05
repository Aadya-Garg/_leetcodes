class Solution:
    def reverseWords(self, s: str) -> str:
       res_l = s.split(" ")
       s = ""
       for elem in res_l:
        if elem != "":
            s = elem + " " + s
       return s.rstrip()