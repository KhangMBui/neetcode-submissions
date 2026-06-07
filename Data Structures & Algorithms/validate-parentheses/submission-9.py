class Solution:
    def isValid(self, s: str) -> bool:
        # solution: create a closeToOpen dict
        closeToOpen = { ")" : "(", "}" : "{", "]": "["}
        stack = []
        #iterate the string, if it's the close, we pop. otherwise push
        for c in s :
            if (c in closeToOpen):
                if (stack and stack[-1] == closeToOpen[c]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
        