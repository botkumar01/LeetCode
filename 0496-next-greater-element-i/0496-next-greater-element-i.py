class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hasi = {}
        l=0
        ans = []
        for i in nums2:
            if i in nums1:
                hasi[i] = l
            l+=1
        for i in nums1:
            add= False
            for j in range(hasi[i],len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    add = True
                    break
            if add==False:
                ans.append(-1)
        return ans         