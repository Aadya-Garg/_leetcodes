class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        left = 0
        len_ = len(arr)
        done = True
        while left <= len_ - k*m:
            for i in range(k - 1):
                for j in range(m):
                    if arr[left + i*m + j] != arr[left + j + i*m + m]:
                        done = False
                        break
                if done == False:
                    break
            if done:
                return True
            done = True
            left += 1
        return False

            