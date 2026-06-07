class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, height)
        for i, h in enumerate(heights):
            start = i
            #once towering over, calculate the area of the previous bar
            while (stack and h < stack[-1][1]):
                preInd, preH = stack.pop()
                maxArea = max(maxArea, preH * (i - preInd))
                start = preInd
            stack.append((start, h))
        # The ones that are left are the ones that last until the end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea