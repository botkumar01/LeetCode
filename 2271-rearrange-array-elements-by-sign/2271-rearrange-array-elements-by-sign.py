class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        a= 0
        b=1
        arr = [0]*(len(nums))
        for i in nums:
            if i<0:
                arr[b] = i
                b+=2
            else:
                arr[a] = i
                a+=2
        return arr