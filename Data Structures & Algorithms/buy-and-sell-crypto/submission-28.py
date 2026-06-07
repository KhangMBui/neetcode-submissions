class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        for r in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if (prices[l] >= prices[r]):
                l = r
        return maxProfit