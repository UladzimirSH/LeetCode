from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        buy_amount = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy_amount:
                buy_amount = prices[i]
                continue
            temp_profit = prices[i] - buy_amount
            if temp_profit > max_profit:
                max_profit = temp_profit

        return max_profit
