class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # use recursion to solve this problem since
        # there are many cases that we need to go back for
        # Rules: Only add parenthesis when open == close == n
        # Only add ( when open < n
        # Only add ) when close < open
        stack = []
        res = []
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


