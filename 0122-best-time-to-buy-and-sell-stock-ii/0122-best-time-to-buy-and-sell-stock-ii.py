class Solution:
    def buynotbuy(self,index,buy,prices,dp)->int:
        if index==len(prices):
            return 0
        if dp[index][buy]!=-1:
            return dp[index][buy]
        if buy==0:
            opt1=0+self.buynotbuy(index+1,0,prices,dp)
            opt2=-prices[index]+self.buynotbuy(index+1,1,prices,dp)
            profit=max(opt1,opt2)
        if buy==1:
            opt1=0+self.buynotbuy(index+1,1,prices,dp)
            opt2=prices[index]+self.buynotbuy(index+1,0,prices,dp)
            profit=max(opt1,opt2)
        dp[index][buy]=profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*(2) for _ in range (n)]
        ans=self.buynotbuy(0,0,prices,dp)
        return ans


        