class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Solution: window frame: (0, 1)
        #if prices on the right is higher: move right
        #else: left -> right
        l, r = 0, 1
        maxProfit = 0
        while (r < len(prices)):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if (prices[r] > prices[l]):
                r += 1
            else:
                l = r
                r += 1
            
        return maxProfit
            