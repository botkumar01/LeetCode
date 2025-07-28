class Solution(object):
    def merge(self, nums1, a,nums2,b):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if b==0:
            return a
        if len(nums2) == len(nums1):
            nums1[:] = nums2
            return
        np = len(nums2)-1
        mp =len(nums1)- len(nums2)-1
        
        cn  = len(nums1)-1
        while np >=0 and mp >=0:
            if nums2[np] >nums1[mp]:
                nums1[cn] = nums2[np] 
                cn-=1
                np-=1
            else:
                nums1[cn] = nums1[mp]
                cn -=1
                mp-=1
        while np>=0:
            nums1[cn] = nums2[np]
            np-=1
            cn-=1
        return