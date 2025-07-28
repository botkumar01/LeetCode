class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums)
        ha = {}
        ans = set()
        for i in nums:
            ha[i] = ha.get(i,0)+1
            if ha[i] > n/3:
                ans.add(i)
        ans = list(ans)
        return ans