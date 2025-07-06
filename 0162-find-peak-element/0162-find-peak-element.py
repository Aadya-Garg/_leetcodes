class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if (length == 1):
            return 0

        if (length == 2) and nums[1] < nums[0]:
            return 0
        elif length == 2:
            return 1
        else:
            left = 0
            right = left + 2

        if nums[1] < nums[0]:
           return 0

        if nums[-1] > nums[-2]:
            return length - 1

        while (left < right and right < length):
            if nums[left + 1] > nums[left] and nums[left+1] > nums[right]:
                return left + 1

            left += 1
            right += 1
        
        