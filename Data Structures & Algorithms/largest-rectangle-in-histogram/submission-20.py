class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, height)
        for i, h in enumerate(heights):
            start = i
            #once towering over, get the previous area
            while (stack and h < stack[-1][1]):
                preInd, preH = stack.pop()
                maxArea = max(maxArea, (i - preInd) * preH)
                start = preInd
            stack.append((start, h))
        #The one that remains in the stack
        #is the one that lasts until the end
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea