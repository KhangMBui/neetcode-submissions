class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to store 
        # ([{}])
        # Perhaps we coult create a dictionary called OpenToClose
        # { '(' : ')', etc.}
        # If ( goes in, we input ) => stack = [ ')', ']', '}' ]
        # Then next time, when we have the closing parenthesis: '}'
        # If stack[-1] == that closing parenthesis, we do stack.pop()
        # Else, return False
        # At the end, if we pass through all things ==> return True
        if not s:
            return True
        
        openToClose = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        return True if not stack else False