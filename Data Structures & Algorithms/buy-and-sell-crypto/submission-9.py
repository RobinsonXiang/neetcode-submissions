class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = 1000
        for i in range(len(prices)):

            profit = prices[i] - lowest_price
            
            if prices[i] < lowest_price:
                lowest_price = prices[i]

            if profit > max_profit:
                max_profit = profit

        return max_profit

