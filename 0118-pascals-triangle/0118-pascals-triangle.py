class Solution(object):
    def generate(self, N):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if N==1:
            return[[1]]
        elif N==2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(N-2):
            add = [1]
            for j in range(len(ans[-1])-1):
                add.append(ans[-1][j] + ans[-1][j+1])
            add.append(1)
            ans.append(add)
        return ans