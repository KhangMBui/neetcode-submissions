class Solution:
    def isValid(self, s: str) -> bool:
        # Solution: create an open to close hashmap
        openToClose = { ')': '(', ']': '[', '}': '{'}
        stack = []
        for item in s:
            if item in openToClose:
                if stack and stack[-1] == openToClose.get(item):
                    print(stack[-1])
                    print(openToClose.get(item))
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return not stack