class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0
        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1

        res = curr_count
        while l + k < len(s):
            if s[l] in vowels:
                curr_count -= 1
            if s[l + k] in vowels:
                curr_count += 1
            l += 1
            res = max(res, curr_count)
        return res