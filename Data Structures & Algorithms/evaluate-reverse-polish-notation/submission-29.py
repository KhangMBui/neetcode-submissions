class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for item in tokens:
            if item == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif item == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif item == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif item == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(float(b) / a))
            else:
                stack.append(item)
        return int(stack[-1])