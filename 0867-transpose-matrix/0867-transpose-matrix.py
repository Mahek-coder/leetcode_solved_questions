class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        new_matrix=[[0]*len(matrix) for i in range(len(matrix[0]))]
        listt,val=[],0
            
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                new_matrix[i][j]=matrix[j][i]
                val+=1
        return new_matrix