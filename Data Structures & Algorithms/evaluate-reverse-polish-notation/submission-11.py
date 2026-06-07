class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #solution: create a stack and evaluate each token
        #if operation, perform on the last two values in the stack
        #if number, push
        stack = []
        for item in tokens:
            if (item == '+'):
                stack.append(stack.pop() + stack.pop())
            elif (item == '-'):
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif (item == '/'):
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b/a)))
            elif (item == '*'):
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(item))
        return stack[-1]