class Solution(object):
    def merge(self, a, m, b, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return a
        cnt = 0 
        i=0
        for _ in range(n):
            a.pop()
        while (cnt!=n and i!=len(a)):
            if a[i] >= b[cnt]:
                
                a.insert(i,b[cnt])
                cnt+=1
            i+=1
        while (cnt!=n):
            a.insert(i,b[cnt])
            i+=1
            cnt+=1
        # for i in range(n):
        #     a.pop()
