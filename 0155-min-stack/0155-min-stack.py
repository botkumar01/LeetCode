class MinStack(object):

    def __init__(self):
       self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
           self.stack.pop()

    def top(self):
        if not self.stack:
           return None
        return self.stack[-1]

    def getMin(self):
        if not self.stack:
            return None
        return min(self.stack)
