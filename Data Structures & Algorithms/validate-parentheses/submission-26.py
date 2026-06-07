class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = { ')' : '(', '}' : '{', ']' : '['}
        stack = []
        for item in s:
            if (stack and stack[-1] == openToClose.get(item)):
                stack.pop()
            else:
                stack.append(item)
        return not stack