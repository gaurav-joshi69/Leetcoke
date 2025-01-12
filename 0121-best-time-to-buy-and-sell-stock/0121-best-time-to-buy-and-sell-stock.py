class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=int(-1e9)
        minprice=int(1e9)
        n=len(prices)
        for i in range(n):
            minprice=min(minprice,prices[i])
            maxprofit=max(maxprofit,prices[i]-minprice)
        return maxprofit
        