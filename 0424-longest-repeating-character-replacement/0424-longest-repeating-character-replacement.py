class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count =0
        maxi=0
        maxf=0
        right=0
        left=0
        hash={}
        n=len(s)
        while right<n:
            hash[s[right]]=hash.get(s[right],0)+1
            maxf=max(maxf,hash[s[right]])
            if right-left+1-maxf>k:
                hash[s[left]]-=1
                if hash[s[left]]==0:
                    del hash[s[left]]
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
            
                



        