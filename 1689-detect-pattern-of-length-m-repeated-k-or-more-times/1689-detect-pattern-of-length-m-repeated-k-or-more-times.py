class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        left = 0
        #right = left + m - 1
        len_ = len(arr)
        #count = 1
        done = True
        print(len_ - k*m)
        while left <= len_ - k*m:
            #print(count)
            for i in range(k - 1):
                for j in range(m):
                    if arr[left + i*m + j] != arr[left + j + i*m + m]:
                        done = False
                        break
                if done == False:
                    break
            if done:
                return True
            #else:
                #count = 1
                #done = True
            done = True

            #if count == k:
            #    return True
            left += 1
            #right += 1
        return False

            