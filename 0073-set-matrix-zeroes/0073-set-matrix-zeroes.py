class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        cl = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    cl.append(j)
        row = set(row)      
        cl = set(cl)
        print(cl,row)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0 

        for j in range(len(matrix)):
            for i in cl:
                matrix[j][i]=0 
                                        
        