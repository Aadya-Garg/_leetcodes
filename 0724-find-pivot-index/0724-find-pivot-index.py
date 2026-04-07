class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        upto_ex = 0
        after = [0]
        for j in range(len(nums) - 1, -1 , -1):
            upto_ex += nums[j]
            after.append(upto_ex)
        upto_ex = 0    
        for i in range(len(nums)):
            upto_ex += nums[i]
            if upto_ex == after[- (i + 1)]:
                return i
        return -1