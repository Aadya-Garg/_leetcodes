class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        #maximize sum of at most k vals
        #should have common vertex
        if k == 0 or edges == []:
            return max(vals)
        edges.sort()
        len_ = len(vals)
        #print(edges)
        dict_ = {key:[] for key in range(len_)}
        for i,j in edges:
            dict_[i].append(j)
            dict_[j].append(i)
              
        print(dict_)
        new_dict = dict()

        def max_fornode(list_):
            max_sum = 0
            heap = list_
            heapq._heapify_max(heap)
            for i in range(k):
                if not heap:
                    break
                curr = heapq._heappop_max(heap)
                max_sum = max(max_sum, max_sum + curr)
            return max_sum
        res = -10000
        for i in dict_:
            list_ = [vals[j] for j in dict_[i]]
            res = max(res, vals[i], vals[i] + max_fornode(list_))
        return res
            
        
        
