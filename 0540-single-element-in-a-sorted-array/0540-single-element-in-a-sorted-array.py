class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) % 2 ==0:
            return-1
        elif len(nums) == 1:
            return nums[0] 
        high = len(nums)
        low = 0
        while low<=high:
            mid = (low+high)//2
            # if mid%2 != 0:
            if mid-1 >= 0 and nums[mid-1] == nums[mid]:
                if  mid % 2 != 0:
                    low = mid+1
                else:
                    high = mid-1
            elif mid +1 < len(nums) and nums[mid+1] == nums[mid]:
                if  mid%2 != 0:
                    high = mid-1
                else:
                    low = mid +2
            else:
                return nums[mid]
        