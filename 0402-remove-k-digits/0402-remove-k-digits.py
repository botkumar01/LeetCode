class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st = []
        for i in num:
            # if len(st) == 0:
            #     st.append(i)
            # else:
            while len(st)>0 and st[-1] > i and k != 0:
                
                st.pop()
                k-=1
                
            st.append(i)
        while k!=0:
            st.pop()
            k-=1
        if st ==[]:
            return "0"
        else:
            st = st[::-1]
            while st and st[-1] =="0":
                st.pop()
        if st ==[]:
            return "0"
        return (''.join(st))[::-1]
