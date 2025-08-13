class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #minimizing problem
        curr1 = sum(nums1)
        curr2 = sum(nums2)
        zer1 = nums1.count(0)
        zer2 = nums2.count(0)
        min1 = curr1 + zer1
        min2 = curr2 + zer2
       
        if min1 == min2:
            return min1

        if zer1 > 0 and min2 > min1:
            return min2

        if zer2 > 0 and min1 > min2:
            return min1
        
        return -1