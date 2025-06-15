class Solution(object):
    def maxScore(self, cp, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        r = len(cp)
        l = k
        total = sum(cp[:l])
        maxi = total

        for i in range(k):
            l-=1
            r-=1
            total -= cp[l]
            total +=  cp[r]
            maxi = max(total,maxi)

        return maxi