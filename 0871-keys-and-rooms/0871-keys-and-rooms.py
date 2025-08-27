class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #q = deque(rooms)
        current = 0
        visited = [0]
        length = len(rooms)
        stack = [rooms[0]]
        print(stack)
        while stack:
            available_keys = stack.pop()
            
            for i in available_keys:
                if i not in visited:
                    stack.append(rooms[i])
                    visited.append(i)
            if len(visited) == length:
                return True
        return len(visited) == length

        """
        for i in range(length):
            keys = keys.union(set(q.popleft()))
            
            print(current, keys)
            if (current+1) in keys:
                current += 1
                continue
            else:
                return False
        """