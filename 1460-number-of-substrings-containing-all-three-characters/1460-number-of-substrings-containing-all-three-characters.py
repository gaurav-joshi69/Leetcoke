class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen={'a':-1,'b':-1,'c':-1}
        count=0
        n=len(s)
        for i in range(n):
           lastseen[s[i]]=i
           lastindex=min(lastseen.values())
           count+=lastindex+1
        return count
