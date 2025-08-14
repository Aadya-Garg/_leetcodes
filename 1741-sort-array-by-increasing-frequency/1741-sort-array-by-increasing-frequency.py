class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        set_ = set(nums)
        dict_ = {key: 0 for key in set_}

        for i in nums:
            dict_[i] += 1
            
        dict_ = [[key, val] for val, key in dict_.items()]
        dict_.sort(key = lambda x: (x[0], -x[1]))
        res = []
        for i,j in dict_:
            res.extend([j]*i)
        return res


        
        



 
