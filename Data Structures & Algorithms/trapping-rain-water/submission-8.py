class Solution:
    def trap(self, height: List[int]) -> int:
        #Solution: keeping maxL and maxR and minus by height[l/r]
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while ( l < r ):
            if (maxL < maxR):
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res