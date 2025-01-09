class Solution:
    def getlong(self ,index1,index2,s,r,dp):
        if index1<0 or index2<0:
            return 0
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        if s[index1]==r[index2]:
            dp[index1][index2]=1+self.getlong(index1-1,index2-1,s,r,dp)
        else:
            dp[index1][index2]=max(self.getlong(index1-1,index2,s,r,dp),self.getlong(index1,index2-1,s,r,dp))
        return dp[index1][index2]
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        r=s[::-1]
        dp=[[-1]*(n) for _ in range(n)]
        return self.getlong(n-1,n-1,s,r,dp)
        #find longest commomn subsequence between string and reversed string 
