class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        ind = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[ind-1]:
                nums[ind]=nums[i]
                ind+=1
        return ind