class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0
        r = len(s) - 1
        arr = list(s)
        while l < r:
            left_v = s[l].lower() in vowels
            right_v = s[r].lower() in vowels

            if left_v and right_v:
                # s = s[:l] + s[r] + s[l + 1: r] + s[l] + s[r+1:]
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
                l += 1
                r -= 1

            elif not left_v:
                l += 1

            else:
                r -= 1

        return "".join(arr)
            