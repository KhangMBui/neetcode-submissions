class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create a result stack of 0 with equal length to temp
        #The key is to have a stack of pair temp - index
        #Iterate through the stack and when a larger temp
        #than the previous one (top of the stack) are met
        #we substract the indexes to find number of days
        stack = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while (stack and t > stack[-1][0]):
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            #append the pair of temp - index
            stack.append((t, i))
        return res
        