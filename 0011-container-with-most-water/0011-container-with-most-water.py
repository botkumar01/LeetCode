class Solution(object):
    def maxArea(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r = len(arr)-1
        ans = 0
        mini=0
        while l<r:
            mini = min(arr[l],arr[r])
            maxi = max(arr[l],arr[r])
            ans = max(ans,(mini*(r-l)))
            while l<r and mini >= arr[l]:
                l+=1
            while l<r and mini >= arr[r]:
                r-=1
        return ans