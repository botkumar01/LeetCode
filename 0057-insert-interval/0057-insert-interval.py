class Solution(object):
    def insert(self, inter, newin):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        arr=[]
        if inter == []:
            return [newin]
        for i in range(len(inter)):
            if inter[i][1] >= newin[0]:
                pick = i
                if inter[i][0] > newin[0]:
                    arr = [newin[0]]
                else:
                    arr = [inter[i][0]]
                break
            else:
                print ans
                ans.append(inter[i])
        if len(arr)==0:
            inter.append(newin)
            return inter
        for i in range(pick,len(inter)):
            if inter[i][1] >= newin[1]:
                if inter[i][0] <= newin[1]:
                    pick = i+1
                    arr.append(inter[i][1])
                else:
                    pick = i
                    arr.append(newin[1])
                break
        if len(arr)==1:
            arr.append(newin[1])
            ans.append(arr)
            return ans
        ans.append(arr)
        for i in range(pick,len(inter)):
            ans.append(inter[i])
        
        return ans