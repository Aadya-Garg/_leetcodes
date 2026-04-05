class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        char = chars[0]
        
        for i in range(1, len(chars)):
            temp_ind = 1
            if chars[i] == char:
                count += 1
                chars[i] = " "
                continue
            char = chars[i]

            if count > 1:  
                while count > 0:
                    chars[i - temp_ind] = str(count%10)
                    count = count // 10
                    temp_ind += 1

                count = 1
        
        temp_ind = 1
        if chars[-1] == " ":
            while count > 0:
                chars[-temp_ind] = str(count%10)
                count = count // 10
                temp_ind += 1
        
        while " " in chars:
            chars.remove(" ")
    