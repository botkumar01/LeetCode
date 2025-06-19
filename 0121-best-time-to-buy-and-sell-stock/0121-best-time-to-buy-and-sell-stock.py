class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        right = len(nums)-1
        left = right -1
        ans = 0
        while left>=0:
            diff  = nums[right] -nums[left]
            if diff <0:
                right = left
                left -=1
            else:
                left -=1
            ans = max(diff,ans)
        return ans