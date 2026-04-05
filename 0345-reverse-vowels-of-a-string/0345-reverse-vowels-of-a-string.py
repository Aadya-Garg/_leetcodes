class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        curr = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                curr.append(s[i])
        len_ = len(s)        
        for i in range(len_):
            if len(curr) == 0:
                return s

            if s[i].lower() in vowels:
                s = s[:i] + curr.pop() + s[i+1:]
        return s 