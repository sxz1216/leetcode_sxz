class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.MinStack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.MinStack) == 0 or x < self.MinStack[-1]:
            self.MinStack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.isEmpty():
            if self.top() == self.MinStack[-1]:
                self.MinStack = self.MinStack[:-1]
            self.stack = self.stack[:-1]
            

    def top(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.MinStack[-1]
        
    def isEmpty(self):
        return len(self.stack) < 1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()