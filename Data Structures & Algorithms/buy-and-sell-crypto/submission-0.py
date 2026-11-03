class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        r = 1

        min_seen = prices[0]
        while r < len(prices):
            res = max(res, prices[r] - min_seen)

            if prices[r] < min_seen:
                min_seen = prices[r]
            r += 1
        return res
        