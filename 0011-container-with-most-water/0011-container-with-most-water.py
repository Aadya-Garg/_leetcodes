class Solution:
    def maxArea(self, height: List[int]) -> int:
        #max base * height
        #should start from farthest
        #brute force is taking cross product and then finding max area
        #prefic suffix?
        length = len(height)
        max_area = 0
        #take prev_max and then start j from min base such
        for i in range(length):
            if (height[i] == 0):
                continue
            min_base = max(1, max_area//height[i])
            #print(height[i], min_base)
            if(i + min_base >= length):
                continue
            for j in range(i + min_base, length):
                #print("looping j...")
                height_ = min(height[i], height[j])
                base = j - i
                max_area = max(max_area, height_*base)
        return max_area
            


        