class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        set_ = set(nums)
        set_ = sorted(set_)
        len_ = len(set_)
        dict_ = {key: 0 for key in set_}
        for i in nums:
            dict_[i] += 1
        print(dict_)
        ind = 0
        res = 0
        """
        def maxprice(n):
            if n < 0:
                return 0
            curr_price = set_[n] * dict_[set_[n]]
            if n == 0:
                return curr_price
            if set_[n-1] == set_[n] - 1:
                return max(curr_price + maxprice(n - 2), maxprice(n - 1))
            return curr_price + maxprice(n - 1)
        return maxprice(len_ - 1)
        """
        max_prices = [0]*len_
        prev = None
        for i in range(len_):
            curr = set_[i]
            freq = dict_[curr]
            price = curr * freq
            if prev is None:
                max_prices[i] = price
    
            elif prev != curr - 1:
                max_prices[i] = price + max_prices[i - 1]
                
            else: #i >= 2
                max_prices[i] = max(price + max_prices[i - 2], max_prices[i - 1])
            
            prev = curr
        return max_prices[-1]
        """
        for i in set_:
            
        while ind < len_:
            curr = set_[ind]
            freq = dict_[curr]
            res += curr * freq
            print(f"addedd to res: {curr, freq}")
            if ind < len_ - 1 and set_[ind+1] == curr - 1:
                prev_ = set_[ind+1]
                if dict_[prev_] <= freq:
                    ind += 2
                else:
                    if (ind + 2 < len_ and set_[ind+2] == curr - 2):
                        if res + (set_[ind+2] * dict_[set_[ind+2]]) > prev_ * dict_[prev_]:
                            ind += 2 #check this
                            continue
                    
                    res -= curr * freq
                    ind += 1
                    #res -= curr * freq
                    print(f"removed from res: {curr, freq}")
            else:
                ind += 1
        return res
        """