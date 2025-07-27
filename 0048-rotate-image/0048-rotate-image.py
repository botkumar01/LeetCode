class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for j in range(len(matrix)):
            for i in range(j,len(matrix)):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]