class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: Initial window frame: (0, 1)
        # Calculate maxProfit
        # if right price > left price: keep moving rightward
        # else: l = r, move rightward
        l, r = 0, 1 
        maxProfit = 0
        while ( r < len(prices) ):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if (prices[r] > prices[l]):
                r += 1
            else:
                l = r
                r += 1
        return maxProfit