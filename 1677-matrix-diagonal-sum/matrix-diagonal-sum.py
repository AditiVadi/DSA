class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat[0])-1
        c=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
        # print(mat[i][j])
                if i==j:
                    c+=mat[i][j]
                elif i+j==n:
                    c+=mat[i][j]
        return c
                
        