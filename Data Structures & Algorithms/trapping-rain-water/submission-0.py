class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]
        maxLeftNum = 0
        maxRight = [0]
        for i in range(1, len(height)):
            maxLeft.append(max(height[i - 1], maxLeftNum))
            maxLeftNum = max(height[i - 1], maxLeftNum)
        maxRightNum = 0
        for i in range(len(height) - 2, -1, -1):
            maxRight.append(max(height[i + 1], maxRightNum))
            maxRightNum = max(height[i + 1], maxRightNum)
        maxRight.reverse()
        minLR = []
        res = 0
        for i in range(len(maxLeft)):
            minLR.append(min(maxLeft[i], maxRight[i]))
            if (minLR[i] > height[i]):
                minLR[i] -= height[i]
            else:
                minLR[i] = 0
            res += minLR[i]
        return res
        
        