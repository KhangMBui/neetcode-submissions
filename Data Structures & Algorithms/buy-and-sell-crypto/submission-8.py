class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Solution: Window frame starts at [0, 1]
        #If price on the right higher => get profit
        #else: move left to right
        l, r = 0, 1
        maxProfit = 0
        while (r < len(prices)):
            if (prices[l] < prices[r]):
                maxProfit = max(maxProfit, prices[r] - prices[l])
            elif (prices[l] > prices[r]):
                l = r
            r += 1
        return maxProfit