class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1

        res = curr_count
        for l in range(len(s) - k):
            if s[l] in vowels:
                curr_count -= 1
            if s[l + k] in vowels:
                curr_count += 1
            res = max(res, curr_count)
        return res