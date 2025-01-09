class Solution:
    def getmaxsub(self,index1,index2,text1,text2,dp):
        if index1<0 or index2<0:
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        if text1[index1]==text2[index2]:
            dp[index1][index2]=1+self.getmaxsub(index1-1,index2-1,text1,text2,dp)
        else:
            dp[index1][index2]=max(self.getmaxsub(index1-1,index2,text1,text2,dp),self.getmaxsub(index1,index2-1,text1,text2,dp))

        return dp[index1][index2]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for j in range(m)] for i in range(n)]
        return self.getmaxsub(n-1,m-1,text1, text2, dp)
        