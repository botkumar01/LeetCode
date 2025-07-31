class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=0
        while l!=len(nums) and nums[l]<=0:
            l+=1
   
        i=1
        while l<len(nums):
            if nums[l] != i:
                print(l)
                return i
            l+=1
            i+=1
            while l<len(nums)-1 and nums[l] ==nums[l-1]:
                print(l)
                l+=1
        # print(nums)  
        print(l)  
        return i