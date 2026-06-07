class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Solution: 
        stack = [] #(index, height)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            #When meet lower, we immediate calculate area
            while (stack and h < stack[-1][1]):
                preIndex, preHeight = stack.pop()
                maxArea = max(maxArea, preHeight * (i - preIndex))
                start = preIndex
            stack.append((start, h))
        print(stack)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea