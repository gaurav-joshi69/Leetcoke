class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        lsum=0
        rsum=0
        tsum=0
        i=0
        for i in range(k):
            lsum+=cardPoints[i]
        tsum=lsum
        maxi=tsum
        right=n-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[right]
            right-=1
            tsum=lsum+rsum
            maxi=max(tsum,maxi)
        return maxi
