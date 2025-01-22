class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        copen=0
        count=0
        for char in range(len(s)):
            if s[char]=='(':
                copen+=1
            elif s[char]==')' and copen >0:
                copen-=1
            else:
                count+=1
        if copen!=0:
            return count+copen
        return count

        