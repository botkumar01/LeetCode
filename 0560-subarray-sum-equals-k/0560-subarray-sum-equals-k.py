class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        hashi = {0:1}
        tar = 0
        for i in range (len(nums)):
            total += nums[i]
            if total - k in hashi:
                tar += hashi[total-k]
           
            # else:
            hashi[total]= hashi.get(total,0)+1
        return tar