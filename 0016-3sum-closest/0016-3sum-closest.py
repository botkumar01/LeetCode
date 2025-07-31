class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 99999999999
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l< r:
                total = nums[i] + nums[l]+ nums[r]
                diff =abs(total-target)
                if diff < ans:
                    ans = diff
                    k = nums[i] + nums[l]+ nums[r]
                if total > target:
                    r-=1
                else:
                    l+=1
        return k