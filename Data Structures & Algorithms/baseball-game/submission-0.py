class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # [1, 2, +, C, 5, D]
        # => [1, 2, 3], + => [3]
        # [1, 2, 3, C] => Invalidate => [1, 2]
        # [1, 2, 5, D] => [1, 2, 5, 10]; 1 + 2 + 5 + 10 = 18

        # UMPIRE
        # Plan: Use a stack. Put stuff in. If ran into +, get the last
        # 2 items and plus them
        # Ran into C: pop last item
        # Ran into D: peek last item, multiply by 2, and append into stack
        
        # Edge case: empty input
        if not operations:
            return 0
        
        stack = []

        for operation in operations:
            if len(stack) >= 2 and operation == '+':
                stack.append(stack[-1] + stack[-2])
            elif stack and operation == 'C':
                stack.pop()
            elif stack and operation == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
        
        return sum(stack)