class RecentCounter:

    def __init__(self):
        #self.requests = deque()
        self.requests = []
        self.start = 0
        self.end = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.end += 1
        #range is [t - 3000, t]
        lower = t-3000
        while self.requests[self.start] < lower:
            self.start += 1
        return self.end - self.start
        """
        while self.requests:
            if self.requests[0] < lower:
                self.requests.popleft()
            else:
                break
        
        return len(self.requests)
        """


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)