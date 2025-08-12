class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        arr = [None]*(n+1)
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1
        for i in range(3, n+1):
            third = i - 3
            second = i - 2
            first = i - 1
            arr[i] = arr[third] + arr[second] + arr[first]
        return arr[-1]


