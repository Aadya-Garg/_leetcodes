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
        point = None
       
        for i,j in sorted_intervals[1:]:
          
            if i <= prev_j and point is None:
                point = min(prev_j, j)

            elif i <= prev_j and point >= i: #imples point not none
                point = min(point, j)

            #elif point is not None and i <= point:
             #   prev_j = j
            #    continue

            else:
                res += 1
                point = None
            prev_j = j
        return res

            