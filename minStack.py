class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        minElement = self.getMin()
        if minElement == None or x < minElement:
            minElement = x
        self.stack.append((x,minElement))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            # print(stack)
            return self.stack[len(self.stack) - 1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()