class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = len(nums)-1
        ans = []
        for i in range(len(nums)-1):
            l=i+1
            r = len(nums)-1
            while l<r:
                if nums[i] + nums[l]+nums[r] ==0:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r] ])
                    l+=1
                    r-=1
                elif nums[i] + nums[l]+nums[r] < 0:
                    l+=1
                else:
                    r-=1
        return ans