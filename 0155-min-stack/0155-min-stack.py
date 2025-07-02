from Queue import Queue
class MinStack(object):

    def __init__(self):
        self.q = Queue()
        # self.mini = 999999999999999999
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.put(val)

    def pop(self):
        """
        :rtype: None
        """
        self.q.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.q.qsize()==0:
            return None
        else:
            return self.q.queue[-1]

    def getMin(self):
        """
        :rtype: int
        """
        self.mini = 999999999999999999

        for i in (list(self.q.queue)):
            self.mini = min(self.mini,i)
        return self.mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()