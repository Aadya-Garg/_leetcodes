class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #number of overlapping intervals.
        points.sort(key = lambda x: x[1])
        print(points)
        try: 
            points[1]
        except:
            return 1
        point = points[0][1]
        res = 1
        con = points[1:]
        for i,j in con:
            if point < i:
                res += 1
                point = j
            """
            This is for when sorted normally
            if point >= i:
                point = min(point, j)
            
            else:
                res += 1
                point = j
            """
        return res

            