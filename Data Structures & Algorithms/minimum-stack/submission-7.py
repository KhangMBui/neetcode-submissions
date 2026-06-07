class MinStack:
    #solution: create 2 stacks: minStack and numStack
    def __init__(self):
        self.minStack = []
        self.numStack = []
    def push(self, val: int) -> None:
        self.numStack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.numStack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.numStack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
