class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #number of overlapping intervals.
        sorted_intervals = sorted(points)
        try: 
            points[1]
        except:
            return 1
        prev_j = sorted_intervals[0][1]
        res = 1
        point = prev_j
        con = sorted_intervals[1:]
        for i,j in con:

            if i <= prev_j and point >= i:
                point = min(point, j)
            
            else:
                res += 1
                point = j
            prev_j = j
        return res

            