class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1

        count = 1
        char = chars[0]
        
        for i in range(1, len(chars)):
            temp_ind = 1
            if chars[i] == char:
                count += 1
                chars[i] = " "
                continue

            if count == 1:
                char = chars[i]
                continue
                
            while count > 0:
                chars[i - temp_ind] = str(count%10)
                count = count // 10
                temp_ind += 1

            count = 1
            char = chars[i]
        
        temp_ind = 1
        if chars[-1] == " ":
            while count > 0:
                chars[-temp_ind] = str(count%10)
                count = count // 10
                temp_ind += 1
        
        while " " in chars:
            chars.remove(" ")





        # length = len(chars)
        # if (length == 1):
        #     return len(chars)
        # count = 1
        # prev = chars[0]
        # i = 1
        # while i < length - 1:
        #     if (prev == chars[i]):
        #         count += 1
        #         i += 1
        #         continue

        #     list_ = [prev]+ list(str(count))
        #     prev = chars[i]

        #     if (i - count >= 0):
        #         chars = chars[:i - count] + list_ + chars[i:]
        #     else:
        #         chars = list_+chars[i:]
        #     i += 1
        #     count = 1

        # if chars[-1] == prev:
        #     chars = chars[:i - count] + [prev] + list(str(count + 1))
        # else:
        #     chars = chars[:i - count - 1] + [prev] + list(str(count + 1)) + chars[-1]
        
        # return len(chars)
            

            



