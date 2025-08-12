class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #recurrence is mincost(i) = cost[i] + min(mincost(i -1), mincost(i-2))
        len_ = len(cost)
        """
        def mincost(n):
            if n < 0:
                return 0
            if n == 1 or n == 0:
                return cost[n]
            return cost[n] + min(mincost(n-1), mincost(n -2))
        return min(mincost(len_-1), mincost(len_-2))
        """
        min_costs = [0]*len_
        min_costs[0] = cost[0]
        min_costs[1] = cost[1]
        for i in range(2, len_):
            min_costs[i] = cost[i] + min(min_costs[i-1], min_costs[i-2])
        return min(min_costs[-1], min_costs[-2])