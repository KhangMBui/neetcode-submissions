class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add the string if open = close = n
        # only add open parenthesis if open < n
        # only add close parenthesis if close < open
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
