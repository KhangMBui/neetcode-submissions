class Solution:
    def isValid(self, s: str) -> bool:
        #Solution: Create an open to close hashmap
        if (len(s) == 1):
            return False
        stack = []
        openToClose = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if (c in openToClose ):
                if (stack and stack[-1] == openToClose.get(c)):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
            