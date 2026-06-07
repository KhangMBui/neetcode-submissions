class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Create a stack, go over the list of string
        #if it's number, push to stack
        #if it's the operation, perform it on the top 2 numbers of the stack
        stack = []
        for c in tokens:
            if (c == '+'):
                stack.append(stack.pop() + stack.pop())
            elif (c == '-'):
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif (c == '*'):
                stack.append(stack.pop() * stack.pop())
            elif (c == '/'):
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[-1]