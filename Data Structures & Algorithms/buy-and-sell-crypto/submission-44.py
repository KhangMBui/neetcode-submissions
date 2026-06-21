class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 1, 5, 6, 7, 1]
        # l = 0, r = 1:
        # 1 - 10 = -9 => negative, move l up
        # l = 1, r = 2:  5 - 1 = 4; positive, move r up
        # l = 1, r = 3: 6 - 1 = 5; positive, move r up
        # l = 1, r = 

        if not prices:
            return 0
        
        l, r = 0, 1
        max_profit = float("-inf")

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            elif prices[r] < prices[l]:
                l = r
            r += 1

        return max_profit if max_profit != float("-inf") else 0