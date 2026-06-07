class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if (len(tokens) == 1):
            return int(tokens[0])
        stack = []
        for item in tokens:
            if (item == '+'):
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif (item == '-'):
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif (item == '*'):
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif (item == '/'):
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(float(b) / a))
            else:
                stack.append(item)
        return stack[-1]