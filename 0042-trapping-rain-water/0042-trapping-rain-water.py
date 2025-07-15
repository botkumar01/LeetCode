class Solution(object):
    def trap(self, nums):
        l = 0
        r = len(nums)-1
        ans = 0
        while l <r:
            mini = min(nums[l],nums[r])
            while nums[l] <= nums[r] and l<r:
                mini = max(mini,nums[l])
                point = l+1
                A = (mini-nums[point])
                l = point
                if A < 0 :
                    continue
                else:
                    ans+=A
            mini = min(nums[l],nums[r])
            while nums[r] <= nums [l] and l <r:
                mini = max(mini,nums[r])
                point = r-1
                A = (mini - nums[point])
                r = point
                if A < 0 :
                    continue
                else:
                    ans += A
        return ans