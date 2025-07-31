class Solution(object):
    def search(self, nums, tar):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l=0
        for i in range(len(nums)):
            mid = (l+n)//2
            if nums[mid]==tar:
                return mid
            elif tar > nums[mid]:
                l=mid
            else:
                n=mid
        return -1