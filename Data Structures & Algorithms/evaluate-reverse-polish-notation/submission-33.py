class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        for token in tokens:
            match token:
                case '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                case '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)
                case '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                case '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(float(b / a)))
                case _:
                    stack.append(token)

        return int(stack[-1])