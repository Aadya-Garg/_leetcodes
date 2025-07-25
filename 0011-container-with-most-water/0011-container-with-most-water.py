class Solution:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)
        max_area = 0
        
        for i in range(length):
            if (height[i] == 0):
                continue
            min_base = max(1, max_area//height[i])
            
            if(i + min_base >= length):
                continue

            for j in range(i + min_base, length):
                height_ = min(height[i], height[j])
                base = j - i
                max_area = max(max_area, height_*base)
        return max_area
            


        