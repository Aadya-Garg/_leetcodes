class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        char = chars[read]
        count = 0

        for read in range(0, len(chars) + 1):
            if read < len(chars) and chars[read] == char:
                count += 1
                continue
            
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                count = 1
            char = chars[read] if read < len(chars) else ""
        chars[:] = chars[: write]
        # for i in range(1, len(chars) + 1):
        #     if i < len(chars) and chars[i] == char:
        #         count += 1
        #         chars[i] = " "
        #         continue
        #     char = chars[i] if i < len(chars) else ""
        #     if count > 1:
        #         count_ = list(str(count))
        #         len_ = len(count_)  
        #         chars[i - len_: i] = count_
        #         count = 1
        
        # while " " in chars:
        #     chars.remove(" ")