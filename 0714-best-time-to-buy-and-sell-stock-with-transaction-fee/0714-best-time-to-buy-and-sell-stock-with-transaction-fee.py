class Solution:
    def getprofit(self, index, prices, buy, dp,fee):
        if index >= len(prices):
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        if buy == 0:
            opt1 = self.getprofit(index + 1, prices, 0, dp,fee)
            opt2 = -prices[index]-fee + self.getprofit(index + 1, prices, 1, dp,fee)
            profit = max(opt1, opt2)
        else:
            opt1 = self.getprofit(index + 1, prices, 1, dp,fee)
            opt2 = prices[index] + self.getprofit(index + 1, prices, 0, dp,fee)
            profit = max(opt1, opt2)
        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        ans=self.getprofit(0,prices,0,dp,fee)
        return ans 
        