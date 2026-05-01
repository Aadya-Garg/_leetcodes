class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [1]
          
        def factorial(num):
            for i in range(len(d), num + 1):
                d.append(i * d[i - 1])
            return d[num]
        return int(factorial(m + n - 2)/(factorial(m-1)* factorial(n - 1)))