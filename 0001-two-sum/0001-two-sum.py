class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        mapp = {}
        for i in range(len(nums)):
            
            if target-nums[i] in mapp:
                return [mapp[target-nums[i]],i]
            mapp[nums[i]] = i
            
        return -1