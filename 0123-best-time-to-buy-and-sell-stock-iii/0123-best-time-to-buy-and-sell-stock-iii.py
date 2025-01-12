class Solution:
    def getprofit(self, index, prices, buy, dp, left):
        if index == len(prices) or left == 0:
            return 0

        if dp[index][buy][left] != -1:
            return dp[index][buy][left]

        if buy == 0:
            opt1 = self.getprofit(index + 1, prices, 0, dp, left)
            opt2 = -prices[index] + self.getprofit(index + 1, prices, 1, dp, left)
            profit = max(opt1, opt2)
        else:
            opt1 = self.getprofit(index + 1, prices, 1, dp, left)
            opt2 = prices[index] + self.getprofit(index + 1, prices, 0, dp, left - 1)
            profit = max(opt1, opt2)

        dp[index][buy][left] = profit
        return dp[index][buy][left]

    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        return self.getprofit(0, prices, 0, dp, 2)
