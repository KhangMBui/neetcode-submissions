class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if (len(tokens) == 1):
            return int(tokens[0])
        stack = []
        for item in tokens:
            if (item.isdigit()):
                stack.append(item)
            else:
                if (item == '+'):
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif (item == '-'):
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a) - int(b))
                elif (item == '*'):
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif (item == '/'):
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(int(a) / int(b)))
                else:
                    stack.append(item)
        return stack[0]