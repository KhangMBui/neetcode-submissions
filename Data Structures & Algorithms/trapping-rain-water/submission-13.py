class Solution:
    def trap(self, height: List[int]) -> int:
        #solution: keep track of maxL and maxR
        maxArea = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while (l < r):
            if (maxL < maxR):
                #some logic
                l += 1
                maxL = max(maxL, height[l])
                maxArea += maxL - height[l]
            else:
                #some logic
                r -= 1
                maxR = max(maxR, height[r])
                maxArea += maxR - height[r]
        return maxArea