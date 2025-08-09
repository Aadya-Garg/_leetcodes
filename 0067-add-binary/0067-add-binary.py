class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        a_new = "0"*(l2-l1) + a
        b_new = "0"*(l1-l2) + b
        len_ = max(l1,l2)
        carry = 0
        res = ""
 
        for i in range(len_- 1, -1, -1):
            sum_ = int(a_new[i]) + int(b_new[i]) + carry
            if sum_ == 2:
                carry = 1
                sum_ = 0
            elif sum_ == 3:
                carry = 1
                sum_ = 1
            else:
                carry = 0
            res_ = str(sum_) + res
            res = res_
        if (carry == 1):
            return str(carry) + res
        return res

