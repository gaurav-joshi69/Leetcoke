class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        st = [] 
        for char in s:
            if char == '(':
                if st:
                    res += '('
                st.append('(')
            elif char == ')':
                st.pop()
                if st:
                    res += ')'
        return res
