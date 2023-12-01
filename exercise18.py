class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None
        self.hold = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min is None:
            self.min = val
        elif val <= self.min:
            self.hold.append(self.min)
            self.min = val

    def pop(self):
        """
        :rtype: None
        """
        poped = self.stack.pop()
        if len(self.stack) == 1:
            self.min = self.stack[0]
        elif len(self.stack) == 0:
            self.hold=[]
            self.min = None
        elif poped == self.min:
            self.min = self.hold[-1]
            self.hold.pop()

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        return top

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
