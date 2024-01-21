class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit += prices[sell] - prices[buy]
            buy += 1
            sell += 1
        
        return maxProfit