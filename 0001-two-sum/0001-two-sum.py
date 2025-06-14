class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        # i = 0
        j = 1
        mapp = {}
        for i in range(len(nums)-1):
            if nums[i]+nums[j]==target:
                return [i,j]
            elif target-nums[i] in mapp:
                return [mapp[target-nums[i]],i]
            mapp[nums[i]] = i
            j+=1
        if target-nums[len(nums)-1] in mapp:
            return [mapp[target-nums[len(nums)-1]],len(nums)-1]
        return arr