class RecentCounter:

    def __init__(self):
        self.request_counter = 0
        self.requests = deque()


    def ping(self, t: int) -> int:
        self.request_counter += 1
        self.requests.append(t)
        
        #range is [t - 3000, t]
        lower = t-3000
        while self.requests:
            if self.requests[0] < lower:
                self.requests.popleft()
            else:
                break
        return len(self.requests)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)