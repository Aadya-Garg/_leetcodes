class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        before = 0
        res = 0
        for i in gain:
            before += i
            if before > res:
                res = before
        return res