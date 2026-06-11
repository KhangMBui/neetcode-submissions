class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30, 38, 30, 36, 35, 40, 28]
        # res = [0, 0, 0, 0, 0, 0, 0]
        # Stack: [30]
        # 38 is bigger than stack[-1] => pop stack[-1]; res = [1, 0,...]
        # Stack: [38]
        # Stack: [38, 30]
        # 36, is bigger than stack[-1] => pop stack[-1]; res = [1, 0, 1, ...]
        # Stack: [38, 36] (maybe we include index in with it)
        # Stack: [38, 36, 35]
        # Stack: [38, 36, 35, 40] => Update all of them

        # Key idea: put a tuple, or inner array, as (number, index)
        # Then we'll put in the number as current index - index

        if not temperatures:
            return []
        
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                popped_value = stack.pop()
                res[popped_value[1]] = i - popped_value[1]

            stack.append((t, i)) # (number, index) tuple
        
        return res