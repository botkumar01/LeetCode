class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st = []
        for i in num:
            while st and st[-1] > i and k != 0:
                
                st.pop()
                k-=1
            if st ==[] and i =="0":
                continue   
            st.append(i)
        while st and k!=0 :
            st.pop()
            k-=1
        if st ==[]:
            return "0"
        return (''.join(st))
