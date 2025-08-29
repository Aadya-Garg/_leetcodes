class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hash_ = dict()
        for i in range(n):
            hash_[i] = 0
        for i,j in roads:
            hash_[i] += 1
            hash_[j] += 1

        list_ = []
        for i in hash_:
            list_.append([i, hash_[i]])

        list_.sort(key = lambda x: x[1],reverse=True)

        for i,j in list_:
            hash_[i] = n
            n -= 1
        score = 0
        for i,j in roads:
            score += hash_[i] + hash_[j]
        return score