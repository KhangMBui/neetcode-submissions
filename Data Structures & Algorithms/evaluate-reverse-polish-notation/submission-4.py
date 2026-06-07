class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        for item in tokens:
            if (item == '+'):
                numberStack.append(numberStack.pop() + numberStack.pop())
            elif (item == '-'):
                a, b = numberStack.pop(), numberStack.pop()
                numberStack.append(b - a)
            elif (item == '*'):
                numberStack.append(numberStack.pop() * numberStack.pop())
            elif (item == '/'):
                a, b = numberStack.pop(), numberStack.pop()
                numberStack.append( int (float(b/a)))
            else:
                numberStack.append(int(item))
        return numberStack[0]
        