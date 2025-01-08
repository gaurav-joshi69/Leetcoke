class Solution:
    def countcoins(self,index,dp,coins,amount)->int:
        if index==0:
            if amount%coins[0]==0:
                return amount//coins[0]
            else:
                return int(1e9)
        if dp[index][amount]!=-1:
            return dp[index][amount]
        nottaken=0+self.countcoins(index-1,dp,coins,amount)
        taken=int(1e9)
        if coins[index]<=amount:
          taken=1+self.countcoins(index,dp,coins,amount-coins[index])
        dp[index][amount]= min(taken,nottaken)
        return dp[index][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        result=self.countcoins(n-1,dp,coins,amount)
        return result if result!=int(1e9) else -1
        