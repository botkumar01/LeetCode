class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=1

        product=1
        mx=float('-inf')
        for i in range(len(nums)):
            product*=nums[i]
            mx=max(product,mx)
            if nums[i]==0:
                product=1
        product=1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            mx = max(mx, product)
            if product == 0:
                product = 1
        return mx