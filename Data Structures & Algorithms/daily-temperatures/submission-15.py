class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create a stack of pair: temp - stackInd
        stack = [] #pair: temp - stackInd
        res = [0]*len(temperatures) #result has the same length of the temp list
        for i, t in enumerate(temperatures):
            #if t > top of the stack (latest temp):
            while (stack and t > stack[-1][0]):
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res