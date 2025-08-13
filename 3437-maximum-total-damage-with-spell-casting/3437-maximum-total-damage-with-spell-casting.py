class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
       
        set_ = set(power)
        set_ = sorted(set_)
        dict_ = {key: 0 for key in set_}
        for i in power:
            dict_[i] += 1

        len_ = len(set_)
        """
        def maxdmg(n):
            if n < 0:
                return 0
            curr_dmg = set_[n] * dict_[set_[n]]
            if n == 0:
                return curr_dmg
            if set_[n] == set_[n-1] + 2:
                return max(curr_dmg + maxdmg(n - 2), maxdmg(n - 1))
            if set_[n] == set_[n-1] + 1:
                if n >= 2 and set_[n] == set_[n-2] + 2:
                    return max(curr_dmg + maxdmg(n - 3), maxdmg(n - 1), maxdmg(n - 2))
                else:
                    return max(curr_dmg + maxdmg(n - 2), maxdmg(n - 1))
            return curr_dmg + maxdmg(n - 1)
        return maxdmg(len_ - 1)
        """
        maxdmg = [0] * len_
        maxdmg[0] = set_[0] * dict_[set_[0]]
        if len_ >= 2 and (set_[1] == set_[0] + 1 or set_[1] == set_[0] + 2):
            maxdmg[1] = max(set_[1] * dict_[set_[1]], maxdmg[0])
        elif len_ >= 2:
            maxdmg[1] = set_[1] * dict_[set_[1]] + maxdmg[0]
        else:
            return maxdmg[-1]

        for i in range(2, len_):
            curr = set_[i]
            freq = dict_[curr]
            val = curr * freq
            if curr == set_[i - 1] + 2:
                maxdmg[i] = max(val + maxdmg[i - 2], maxdmg[i - 1])
            elif curr == set_[i - 1] + 1 and curr == set_[i - 2] + 2:
                if i > 2:
                    maxdmg[i] = max(val + maxdmg[i - 3], maxdmg[i - 1], maxdmg[i - 2])
                else:
                    maxdmg[i] = max(val, maxdmg[i - 1], maxdmg[i - 2])
            elif curr == set_[i - 1] + 1:
                maxdmg[i] = max(val + maxdmg[i - 2], maxdmg[i - 1])
            
            else:
                maxdmg[i] = val + maxdmg[i - 1]
        return maxdmg[-1]