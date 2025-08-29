class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hash_ = dict()
        for i in range(n):
            hash_[i] = 0
        for i,j in roads:
            hash_[i] += 1
            hash_[j] += 1
        #I have the number of connections
        #in the end, loop thorugh rooads again for summing
        #nlogn for sorting though
        list_ = []
        for i in hash_:
            list_.append([i, hash_[i]])

        list_.sort(key = lambda x: x[1],reverse=True)
        print(list_)
        for i,j in list_:
            hash_[i] = n
            n -= 1
        score = 0
        for i,j in roads:
            score += hash_[i] + hash_[j]
        return score