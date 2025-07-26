class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        list_ = sorted(list(zip(nums1, nums2)), key = lambda x: x[1], reverse = True)
        heap = []
        res = 0
        sum_ = 0
        for i,j in list_:
            sum_ += i
            heapq.heappush(heap, i)
            if len(heap) > k:
                val = heapq.heappop(heap) #what if 
                sum_ -= val
            if len(heap) == k:
                res = max(res, sum_ * j)
        return res
