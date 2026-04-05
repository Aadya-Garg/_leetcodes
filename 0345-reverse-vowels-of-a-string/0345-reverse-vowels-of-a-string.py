class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0
        r = len(s) - 1
        arr = list(s)
        while l <= r:
            left_v = arr[l].lower() in vowels
            right_v = arr[r].lower() in vowels
            if left_v and right_v:
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
            
        # curr = []
        # for i in range(len(s)):
        #     if s[i].lower() in vowels:
        #         curr.append(s[i])
        # len_ = len(s)        
        # for i in range(len_):
        #     if len(curr) == 0:
        #         return s

        #     if s[i].lower() in vowels:
        #         s = s[:i] + curr.pop() + s[i+1:]
        # return s 