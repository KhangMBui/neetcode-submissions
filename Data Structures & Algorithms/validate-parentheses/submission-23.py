class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { '(' : ')', '{' : '}', '[' : ']' }
        stack = []
        for c in s:
            if (c in closeToOpen):
                stack.append(closeToOpen[c])
            else:
                if (len(stack) != 0 and c == stack[-1]):
                    stack.pop()
                else:
                    return False
        return not stack