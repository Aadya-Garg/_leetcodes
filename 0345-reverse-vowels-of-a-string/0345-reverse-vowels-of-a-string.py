class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I', 'O', 'U']
        vowels_in_s = []
        
        length = len(s)
        for i in s:
            if i in vowels:
                vowels_in_s.append(i)
        
        final = list(s)
        #final = [i if i not in vowels else vowels_in_s.pop() for i in s ]
        for i in range(length):
            char = s[i]
            if char in vowels:
                final[i] = vowels_in_s.pop()
        return ("".join(final))


