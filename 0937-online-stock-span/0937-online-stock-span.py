class StockSpanner(object):

    def __init__(self):
        self.st = []
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        sums= 1
        while self.st and price>= self.st[-1][1]:
            sums += self.st[-1][0]
            self.st.pop()
        self.st.append([sums, price])
        return sums
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)