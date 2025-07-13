class Solution(object):
    def nextGreaterElements(self, nums):
    
        ans = []
        st = []
        for i in range(len(nums)):
            while st:
                if st[-1] <= nums[len(nums)-1-i]:
                    st.pop()
                else:
                    break
            if len(st) == 0:
                ch = False
                for k in range(len(nums)-i):
                    if nums[k] > nums[len(nums)-1-i]:
                        ans.append(nums[k])
                        st.append(nums[k])
                        st.append(nums[len(nums)-1-i])
                        ch = True
                        break
                if ch == False:
                    ans.append(-1)
                    

            else:
                ans.append(st[-1])
            st.append(nums[len(nums)-1-i])
        
        return ans[::-1]