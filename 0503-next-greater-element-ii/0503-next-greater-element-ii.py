class Solution(object):
    def nextGreaterElements(self, nums):
    
        ans = []
        st = []
        for i in nums[::-1]:
            while st:
                if st[-1] <= i:
                    st.pop()
                else:
                    break
            if len(st) == 0:
                ch = False
                for k in nums:
                    if k > i:
                        ans.append(k)
                        st.append(k)
                        st.append(i)
                        ch = True
                        break
                if ch == False:
                    ans.append(-1)
                    

            else:
                ans.append(st[-1])
            
            st.append(i)
        ans = ans[::-1]
        return ans