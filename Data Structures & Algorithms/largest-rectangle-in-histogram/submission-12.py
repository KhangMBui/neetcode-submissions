class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair of index, height
        for i, h in enumerate(heights):
            start = i
            #if stack is not empty
            #if we start towering over, we pop
            while (stack and h < stack[-1][1]):
                previousIndex, previousHeight = stack.pop()
                maxArea = max(maxArea, previousHeight * (i - previousIndex))
                start = previousIndex
            stack.append((start, h))
        #the ones left are the ones that last until the end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

        