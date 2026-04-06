class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        output = 0
        nums.sort()
        while (left < right):
            temp = nums[left] + nums[right]
            if ( temp < k):
                left += 1
            elif (temp > k):
                right -= 1
            else:
                left += 1
                right -= 1
                output += 1
        return output    