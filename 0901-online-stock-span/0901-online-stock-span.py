class StockSpanner:

    def __init__(self):
        self.pastPrices = []
        # since span is cumulative, can store it so can use it

    def next(self, price: int) -> int:
        #--- append price to past for consistency with the problem  
        span = 1
        n = len(self.pastPrices)
        while span <= n:
            prev = self.pastPrices[-span][0]
            if prev > price:
                break
            if prev == price:
                span += self.pastPrices[-span][1]
                break
            span += self.pastPrices[-span][1]
            
        self.pastPrices.append((price, span))
        return span

        # check if previous day's span is already calulcated -> recursive



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)