class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        char = chars[0]
        
        for i in range(1, len(chars) + 1):
            temp_ind = 1
            if i < len(chars) and chars[i] == char:
                count += 1
                chars[i] = " "
                continue
            char = chars[i] if i < len(chars) else ""
            if count > 1:
                count_ = list(str(count))
                len_ = len(count_)  
                chars[i - len_: i] = count_
                count = 1
        
        while " " in chars:
            chars.remove(" ")
        
        # if count > 1:
        #         count_ = list(str(count))
        #         len_ = len(count_)  
        #         chars[i - len_: i] = count_
        #         count = 1
    