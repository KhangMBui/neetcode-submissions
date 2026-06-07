class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Solution: create a backtrack function to go back
        #Solution: add parenthesis when open == close == n
        #Add open when open < n
        #Add close when close < open
        stack = []
        res = []
        def backtrack(openN, closeN):
            if (openN == closeN == n):
                res.append("".join(stack))
                return
            if (openN < n):
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if (closeN < openN):
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return res