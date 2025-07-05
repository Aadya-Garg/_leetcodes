class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        i = 0
        while i < length:
            if nums.count(nums[i]) == 1:
                return nums[i]
            else:
                i += 2