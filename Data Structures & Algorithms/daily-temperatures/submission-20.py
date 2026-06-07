class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create a stack of pair (temp - index)
        stack = [] #pair of (temp - index)
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while (stack and t > stack[-1][0]):
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res