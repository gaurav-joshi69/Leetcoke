class Solution:
    def getmaxprofit(self,index,buy,k,prices,dp):
        if index==len(prices) or k==0:
            return 0
        if dp[index][buy][k]!=-1:
            return dp[index][buy][k]
        if buy==0:
            opt1=0+self.getmaxprofit(index+1,0,k,prices,dp)
            opt2=-prices[index]+self.getmaxprofit(index+1,1,k,prices,dp)
            profit=max(opt1,opt2)
        if buy==1:
            opt1=0+self.getmaxprofit(index+1,1,k,prices,dp)
            opt2=prices[index]+self.getmaxprofit(index+1,0,k-1,prices,dp)
            profit=max(opt1,opt2)
        dp[index][buy][k]=profit
        return dp[index][buy][k]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]
        return self.getmaxprofit(0, 0, k, prices, dp)
