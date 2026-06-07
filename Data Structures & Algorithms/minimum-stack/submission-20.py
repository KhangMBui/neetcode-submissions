class MinStack:

    def __init__(self):
        self.minStack = []
        self.numStack = []

    def push(self, val: int) -> None:
        self.numStack.append(val)
        self.minStack.append(min(val, self.minStack[-1]) if self.minStack else val)

    def pop(self) -> None:
        self.numStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.numStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
