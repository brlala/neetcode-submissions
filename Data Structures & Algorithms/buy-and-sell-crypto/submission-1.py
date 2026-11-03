class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        min_buy = prices[0]
        for sell in prices:
            res = max(res, sell - min_buy)

            if sell < min_buy:
                min_buy = sell
        return res
        