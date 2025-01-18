class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        mp=[]
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    mp.append((i,j))
        while mp:
            row,col=mp.pop()
            for j in range(m):
                matrix[row][j]=0
            for i in range(n):
                matrix[i][col]=0

        """
        Do not return anything, modify matrix in-place instead.
        """
        