class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #number of overlapping intervals.
        sorted_intervals = sorted(points)
        try: 
            points[1]
        except:
            return 1
        point = sorted_intervals[0][1]
        res = 1
        con = sorted_intervals[1:]
        for i,j in con:
            if point >= i:
                point = min(point, j)
            
            else:
                res += 1
                point = j
        return res

            