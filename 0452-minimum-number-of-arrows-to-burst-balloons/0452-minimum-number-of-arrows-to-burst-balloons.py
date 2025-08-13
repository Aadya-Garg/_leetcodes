class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #number of overlapping intervals.
        sorted_intervals = sorted(points)
        try: 
            points[1]
        except:
            return 1
        prev = sorted_intervals[0]
        res = 1
        point = None
        #print(sorted_intervals)
        for i,j in sorted_intervals[1:]:
           # print(f"int: {i,j}, point: {point}, prev = {prev}, res = {res}")
            if i <= prev[1] and point is None:
                #res += 1
                point = min(prev[1], j)
            elif i <= prev[1] and point >= j: #imples point not none
                #res += 1
                point = j
            elif point is not None and i <= point:
                res = res
                #res += 1
            else:
                res += 1
                point = None
            prev = [i,j]
        return res

            