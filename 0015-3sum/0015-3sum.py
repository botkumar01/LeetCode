class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = len(nums)-1
        ans = set()
        for i in range(len(nums)-1):
            l=i+1
            r = len(nums)-1
            # if nums[i] > 0 :
            #     break
            while l<r:
                t =nums[i] + nums[l]+nums[r]
                if t ==0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif t < 0:
                    l+=1
                else:
                    r-=1
                # h[[nums[i],nums[l],nums[r]]] = 0
        # ans = list(ans)
        k = []
        for i in ans:
            k.append(list(i))
        ans = 0
        nums =0 
        return k