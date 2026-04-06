class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 #points to k elements
        r = k #next element to be added to the k elems
        temp_sum = sum(nums[: k])
        res = temp_sum
        while r < len(nums):
            temp_sum = temp_sum - nums[l] + nums[r]
            l += 1
            r += 1
            res = max(res, temp_sum)
        return res/k