class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create a stack of a pair: temperature - index
        #Initialize a result array of 0, same length with temp
        res = [0] * len(temperatures)
        stack = [] # pair: temp - index
        for i, t in enumerate(temperatures):
            #If stack is not empty and the current temperature is bigger
            #than the temp at the top of the stack:
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
        