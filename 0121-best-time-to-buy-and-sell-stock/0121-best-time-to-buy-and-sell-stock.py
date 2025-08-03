class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 0
        max_ = 0
        res = 0
        while prices:
            num = prices.pop()
            if prices == []:
                min_ = min(num, min_)
                res = max(res, max_ - min_)
                break
            if num > max_:
                res = max(res, max_ - min_)
                max_ = num
                min_ = num
            else:
                min_ = min(num, min_)
        return res
