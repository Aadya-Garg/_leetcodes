class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        for i,j in roads:
            degree[i] += 1
            degree[j] += 1

        #ordered = sorted(degree, reverse = True)
        ordered = sorted(range(n), key=degree.__getitem__)
        score = 0
        val = 1
        for i in ordered:
            score += val * degree[i]
            val += 1
        return score