class Solution:
    def decodeString(self, s: str) -> str:
        #stack up only for nested strings
        stack = []
        length = len(s)
        res = ""
        for i in range(length):
            if s[i].isnumeric() and (i - 1 >= 0) and (s[i-1].isnumeric()):
                stack[-1][0] += s[i]
            
            elif s[i].isnumeric():
                stack.append([s[i], "", False])

            elif s[i] == "[":
                continue

            elif s[i] == ']':
                temp_rep, temp_str, _ = stack.pop()
                temp_str = int(temp_rep) * temp_str
                if stack and stack[-1][2] == False:
                    stack[-1][1] += temp_str
                else:
                    res += temp_str
            elif stack:
                #so this char is being repeated
                stack[-1][1] += s[i]
            else:
                res += s[i]
        return res   

