class Solution:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)
        max_area = 0
        left = 0
        right = length - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
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


        