class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if i in arr:
                continue
            elif nums.count(i) == 1:
                return i
            else:
                arr.append(i)
        