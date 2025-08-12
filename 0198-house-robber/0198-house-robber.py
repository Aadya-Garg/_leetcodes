class Solution:
    def rob(self, nums: List[int]) -> int:
        len_ = len(nums)
        #recurive relation: max(maxcost(len - 1), maxcost(len - 2))
        #maxcost(2) = max(maxcost(1), maxcost(1)) + 2
        """
        def maxprice(n):
            if n < 0:
                return 0
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            return max(nums[n] + maxprice(n-2), maxprice(n-1))
        return maxprice(len_-1)
        """
        if len_ == 1:
            return nums[0]
        maxes = [0]*len_
        maxes[0] = nums[0]
        maxes[1] = max(nums[1], nums[0])
        for i in range(2, len_):
            maxes[i] = max(nums[i] + maxes[i - 2], maxes[i-1])
        return maxes[-1]