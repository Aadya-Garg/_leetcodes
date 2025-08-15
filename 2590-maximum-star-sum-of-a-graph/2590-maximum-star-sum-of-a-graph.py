class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        #maximize sum of at most k vals
        #should have common vertex
        if k == 0 or edges == []:
            return max(vals)

        len_ = len(vals)
        #print(edges)
        dict_ = {key:[] for key in range(len_)}
        for i,j in edges:
            dict_[i].append(vals[j])
            dict_[j].append(vals[i])

        def max_fornode(list_):
            max_sum = 0
            heapq._heapify_max(list_)
            for i in range(k):
                if not list_:
                    break
                curr = heapq._heappop_max(list_)
                max_sum = max(max_sum, max_sum + curr)
            return max_sum
        res = -10000
        for i in range(len_):
            list_ = dict_[i]
            res = max(res, vals[i], vals[i] + max_fornode(list_))
        return res
            
        
        
