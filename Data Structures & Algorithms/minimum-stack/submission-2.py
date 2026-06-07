class MinStack:
    def __init__(self):
        self.numberStack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.numberStack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.numberStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.numberStack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
