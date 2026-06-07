class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Solution: We need an array of pair: (temp, index)
        # ((30, 1), (38, 2), (30, 3), (36, 4))
        stack = [] # (temp - index)
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while (stack and t > stack[-1][0]):
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((t, i))
        return res