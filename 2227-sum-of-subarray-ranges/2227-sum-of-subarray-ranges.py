class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i,len(nums)):
                if nums[j] > maxi:
                    ans += nums[j]-mini
                    maxi = nums[j]
                elif nums[j] < mini:
                    mini = nums[j]
                    ans += maxi-mini
                else:
                    ans += maxi-mini
        return ans