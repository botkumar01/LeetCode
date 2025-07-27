class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = set()
        cl = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    cl.add(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0 

        for j in range(len(matrix)):
            for i in cl:
                matrix[j][i]=0 
                                        
        