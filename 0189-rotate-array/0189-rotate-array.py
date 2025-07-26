class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = nums[:]
        k=k%len(nums)
        l = k
        for i in range(k):
            nums[i] = nums[-l]
            l-=1
        p=0
        while k!=len(nums):
            nums[k] = m[p]
            k+=1
            p+=1
        m=0