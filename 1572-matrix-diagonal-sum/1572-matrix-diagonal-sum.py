class Solution(object):
    def diagonalSum(self, mat):
        sum1=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i==j):
                   sum1+=mat[i][j]
                elif(j==len(mat[0])-1-i):
                   sum1+=mat[i][j]
        return sum1