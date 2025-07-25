class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        length = len(nums)
        while left < right and right < length:
            if (nums[left] != 0):
                left += 1
                right += 1
                continue
            if nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
            right += 1
            
        return nums

