class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        n=len(s)
        maxlen=0 
        left=0
        for right in range(n):
            ch=s[right]
            if ch in mp and mp[ch]>=left:
                left=mp[ch]+1
            mp[ch]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen
                

            
                    