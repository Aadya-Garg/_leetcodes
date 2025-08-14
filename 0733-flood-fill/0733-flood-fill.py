class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image
        nrows = len(image)
        ncols = len(image[0])
        done = []
        #update start at the end
        def fill(i,j):
            curr = image[i][j]
            #if curr != start:
            #    image[i][j] = curr
            if curr == start:
                #print(curr)
                image[i][j] = color
                done.append([i,j])
                if i > 0 and [i-1,j] not in done:
                    fill(i-1, j)
                if j > 0 and [i,j-1] not in done:
                    fill(i, j-1)
                if j < ncols - 1 and [i,j+1] not in done:
                    fill(i, j+1)
                if i < nrows - 1 and [i+1,j] not in done:
                    fill(i + 1, j)
        fill(sr, sc)
        
        return image
            
            
            