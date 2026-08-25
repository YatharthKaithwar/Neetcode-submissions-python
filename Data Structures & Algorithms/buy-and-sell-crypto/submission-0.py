class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit= 0

        for price in prices:
            if price < minPrice:#if cur price is less than the minPrice
                minPrice = price # update it 
            elif price-minPrice > maxProfit:#if the profit at curr price
                maxProfit = price - minPrice#greater than prev profit
        return maxProfit