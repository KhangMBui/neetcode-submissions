class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Solution: Create a stack and iterate through the tokens list
        #If operation, perform it on the last 2 numbers in the stack
        stack = []
        for item in tokens:
            if (item == '+'):
                stack.append(stack.pop() + stack.pop())
            elif (item == '-'):
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif (item == '/'):
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a)/b))
            elif (item == '*'):
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(item))
        return stack[0]