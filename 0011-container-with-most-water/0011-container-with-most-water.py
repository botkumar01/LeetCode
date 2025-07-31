class Solution(object):
    def maxArea(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r = len(arr)-1
        ans = 0
        while l<r:
            mini = min(arr[l],arr[r])
            maxi = max(arr[l],arr[r])
            ans = max(ans,(mini*(r-l)))
            if mini == arr[l]:
                l+=1
            else:
                r-=1
        return ans