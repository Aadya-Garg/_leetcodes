class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if n == 0:
        #     return True
        # # --- not all flowers filled yet -----
        # remaining = len(flowerbed)
        # if remaining == 0:
        #     return False

        # if remaining == 1:
        #     return (flowerbed[0] == 0 and n == 1)
        
        # if flowerbed[1] == 1:
        #     return self.canPlaceFlowers(flowerbed[3:], n)

        # if flowerbed[0] == 0 and flowerbed[1] == 0:
        #     flowerbed[0] = 1
        #     n -= 1
        
        # return self.canPlaceFlowers(flowerbed[2:], n)
        
        i = 0
        while i < len(flowerbed):
            if n == 0:
                return True
                
            if i == len(flowerbed) - 1:
                return (flowerbed[i] == 0 and n == 1)

            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 2
                continue
                
            if flowerbed[i+1] == 1:
                i += 3
                continue

            if flowerbed[i] == 1:
                i += 2
        return n == 0