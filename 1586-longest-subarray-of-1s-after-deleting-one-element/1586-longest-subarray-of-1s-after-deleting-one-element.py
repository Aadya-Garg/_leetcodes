class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        try:
            left = nums.index(1)
        except:
            return 0
        length = len(nums)
        max_len = 0
        #print(f"left = {left}")
        #print(f"rest of the array: {nums[left+1:]}")
        try:
            right = nums[left+1:].index(0) + left + 1
        except:
            if (left == 0):
                return length - 1
            return length - left

        temp_len = right - left #number of 1s including left ind
        while (right < length - 1):
           # print(f"left = {left}, right = {right}")
            if nums[right+ 1] == 0:
                #print("running first confiton ...")
                
                temp_len = right - left #includes the 0 to be deleted
                right += 1
                max_len = max(temp_len, max_len)
                left = nums[left+1:].index(0) + left + 1
                try:
                    left = nums[left+1:].index(1) + left + 1
                except:
                    break
                if (left > right):
                    try:
                        right = left + nums[left+1:].index(0) + 1
                    except:
                        right = left
                continue
            else:
                #print("running second confiton ...")
                right += 1
                continue
        print(f"left = {left}, right = {right}")
        return max(max_len, right - left)

            

