class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = len(nums)-1
        ans = []
        h = {}
        for i in range(len(nums)-1):
            l=i+1
            r = len(nums)-1
            if nums[i] > 0 :
                break
            while l<r:
                t =nums[i] + nums[l]+nums[r]
                # if nums[i]>0:
                #     continue
                if t ==0:
                    # if ans[-1] != [nums[i],nums[l],nums[r]]:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif t < 0:
                    l+=1
                else:
                    r-=1
                # h[[nums[i],nums[l],nums[r]]] = 0
        # ans = list(ans)
        return ans