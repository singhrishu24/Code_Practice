'''
Best Day to Buy and sell Stocks 1.
single day to buy and sell stock.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res    
