class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = 1000

        for price in prices:

            profit = price - lowest_price
            lowest_price = min(lowest_price, price)
            max_profit = max(max_profit, profit)

        return max_profit

