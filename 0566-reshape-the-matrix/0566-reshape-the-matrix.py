class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        listt,val=[],0
        if len(mat)*len(mat[0])!=r*c:
            return mat
        for i in mat:
            for j in i:
                listt.append(j)
        matrix=[[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j]=listt[val]
                val+=1
        return matrix