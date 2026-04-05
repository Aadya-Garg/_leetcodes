class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix?
        prod = 1
        res = [1]
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            res.append(prod)
        prod = 1
        for j in range(len(nums)- 1, 0, -1): #j = 3,2,1,0
            prod *= nums[j]
            res[j-1] *= prod
        return res





        #one loop
        # output = []
        # arr_len = len(nums)
        # before = 1
        # after = 1
        # for i in range(arr_len):
        #     output.append(before)
        #     before *= nums[i]
        # for j in range(arr_len - 1, -1, -1):
        #     output[j] *= after
        #     after *= nums[j]
        # return output
            

