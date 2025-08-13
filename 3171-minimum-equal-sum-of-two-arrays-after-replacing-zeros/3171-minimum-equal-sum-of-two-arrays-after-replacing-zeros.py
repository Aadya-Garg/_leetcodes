class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #minimizing problem
        curr1 = 0
        curr2 = 0
        zer1 = 0
        zer2 = 0
        for i in nums1:
            curr1 += i
            if i == 0:
                zer1 += 1
        for j in nums2:
            curr2 += j
            if j == 0:
                zer2 += 1
        #curr1 = sum(nums1)
        #curr2 = sum(nums2)
        #zer1 = nums1.count(0)
        #zer2 = nums2.count(0)
        min1 = curr1 + zer1
        min2 = curr2 + zer2
        print(curr1, curr2)
        print(min1, min2)
        print(zer1, zer2)
        if min1 == min2:
            return min1

        if min2 > min1 and zer1 > 0:
            return min2

        if min1 > min2 and zer2 > 0:
            return min1
        
        return -1