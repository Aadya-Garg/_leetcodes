class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #one loop
        output = []
        arr_len = len(nums)
        before = 1
        after = 1
        for i in range(arr_len):
            output.append(before)
            before *= nums[i]
        for j in range(arr_len - 1, -1, -1):
            output[j] *= after
            after *= nums[j]
        return output
            

