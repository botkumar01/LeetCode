class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = (sorted(set(nums)))
        l=0
        while l!=len(nums) and nums[l]<=0:
            l+=1
   
        i=1
        while l<len(nums):
            if nums[l] != i:
                return i
            l+=1
            i+=1
        return i