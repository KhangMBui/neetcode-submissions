class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #solution: create a backtrack recursive function that
        #adds the parenthesis and goes back to take care of other cases
        #rules: only add parenthesis when open == close == n
        #only add open when open < n
        #only add close when close < open
        res = []
        stack = []
        def backtrack(openN, closeN):
            if (openN == closeN == n):
                res.append("".join(stack))
                return
            if (openN < n):
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            if (closeN < openN):
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return res