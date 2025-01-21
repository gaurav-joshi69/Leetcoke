class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str2=sorted(strs)
        fst=str2[0]
        ans=""
        last=str2[len(str2)-1]
        for char in range(min(len(fst),len(last))):
            if fst[char]!=last[char]:
                return ans 
            ans+=fst[char]
        return ans 
        