class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30, 38, 30, 36, 35, 40, 28]
        # [1, 4, 1, 2, 1, 0, 0]

        # Perhaps at first initialize an array of [0] * len(temperatures)
        # => [0, 0, 0, 0, 0, 0, 0]. This is the res array

        # Then we'll have a stack to put in (value, index)
        # then use a while loop to detect current value > last value in the stack
        # For each, we'll use that last value's index to know its position in res array
        # and result will be current_value_index - last_value_index, 
        # because that's the day difference

        # Edge case: empty input
        if not temperatures:
            return []
        
        res = [0] * len(temperatures)
        stack = [] # (value, index)

        for i, t in enumerate(temperatures):
            # Ejection strategy:
            while stack and t > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((t, i))
        
        return res
        
        