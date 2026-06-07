class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = { "]" : "[", "}" : "{", ")" : "("}
        for item in s:
            if (item in openToClose):
                if (stack and openToClose[item] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return not stack