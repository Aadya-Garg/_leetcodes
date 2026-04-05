class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        original_max = max(candies)
        res = []
        for i in candies:
            res.append(i + extraCandies >= original_max)
        return res