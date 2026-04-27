class Solution:
    def numTilings(self, n: int) -> int:
        mod = int(1e9 + 7)
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5
        for i in range(4, n+1):
            dp[i] = (dp[i-1]*2 + dp[i-3]) % mod
        return dp[n]
        # def dominoes(i, n, possible):
        #     if i == n:
        #         return 0 if possible else 1
        #     if i > n:
        #         return 0
        #     if possible:
        #         return (dominoes(i + 1, n, False) + dominoes(i + 1, n, True)) % mod
        #     return (dominoes(i + 1, n, False) + dominoes(i + 2, n, False) + 2 * dominoes(i + 2, n, True)) % mod
        # return dominoes(0, n, False)    
    