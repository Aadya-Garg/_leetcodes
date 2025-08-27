class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [0]
        length = len(rooms)
        stack = [rooms[0]]
        while stack:
            available_keys = stack.pop()
            
            for i in available_keys:
                if i not in visited:
                    visited.append(i)
                    #if len(visited) == length:
                     #   return True
                    stack.append(rooms[i])
        return len(visited) == length
