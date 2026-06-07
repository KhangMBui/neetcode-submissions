class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Solution: create a def backtrack(openN, closeN)
        #Only add parenthesis when openN == closeN == n
        #Add ) when closeN < openN
        #Add ( when openN < n
        stack = []
        res = []
        def backtrack(openN, closeN):
            if (openN == closeN == n):
                res.append("".join(stack))
                return
            if (closeN < openN):
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()    
            if (openN < n):
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
        backtrack(0, 0)
        return res