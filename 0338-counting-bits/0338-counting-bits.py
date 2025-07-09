class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n + 1)
        for i in range(1, n+1):
            ref = arr[i//2]
            if (i%2 != 0):
                ref += 1
            arr[i] = ref
        return arr
