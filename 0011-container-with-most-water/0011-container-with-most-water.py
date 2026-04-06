class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            temp_h = min(height[l], height[r])
            temp_w = r - l
            res = max(res, temp_h * temp_w)
            #--- how do I move right and left here?
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res





        # length = len(height)
        # max_area = 0
        # left = 0
        # right = length - 1
        # while left < right:
        #     max_area = max(max_area, (right - left) * min(height[left], height[right]))

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_area
        """
        for i in range(length-1):
            if (height[i] == 0):
                continue
            min_base = max(1, max_area//height[i])

            for j in range(i + min_base, length):
                height_ = min(height[i], height[j])
                base = j - i
                max_area = max(max_area, height_*base)
        return max_area
        """


        