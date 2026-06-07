class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution: use maxL and maxR
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        maxArea = 0
        while (l < r):
            if (height[l] < height[r]):
                l += 1
                maxL = max(height[l], maxL)
                maxArea += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                maxArea += maxR - height[r]
        return maxArea