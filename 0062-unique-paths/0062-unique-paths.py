class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = {0: 1}
          
        def factorial(num):
            for i in range(1, num + 1):
                if i not in d:
                    d[i] = i * d[i - 1]
            return d[num]
        return int(factorial(m + n - 2)/(factorial(m-1)* factorial(n - 1)))