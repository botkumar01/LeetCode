class MinStack(object):

    def __init__(self):
        self.min = 99999999999
        self.stack = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min = min(val,self.min)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if len(self.stack) ==0:
            self.min=9999999999
            return None
        # print(self.stack)
        self.min = min(self.stack)
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # print(self.stack)
        return int(self.min)

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()