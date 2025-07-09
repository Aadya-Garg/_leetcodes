class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = [asteroids[-1]]
        length = len(asteroids)
        i = length - 2
        while (i >= 0):
            current = asteroids[i]
            if (arr == []) or (current < 0) or (arr[-1] >= 0):
                arr.append(current)

            elif (abs(arr[-1]) < current):
                arr.pop()
                if (arr == []) or (arr[-1] >= 0):
                    arr.append(current)
                    
                else:
                    continue
            elif (abs(arr[-1]) == current):
                arr.pop()
                
            else:
                i = i
            i -= 1
        arr.reverse()
        return arr

        