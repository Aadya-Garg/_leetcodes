class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        length = len(rooms)
        visited = [False]*length
        stack = [0] #room indices
        seen = 1
        visited[0] = True
        while stack:
            room_ind = stack.pop()
            available_keys = rooms[room_ind]
            
            for i in available_keys:
                if visited[i] == False:
                    seen += 1
                    visited[i] = True
                    stack.append(i)
                if seen == length:
                    return True
        return False
