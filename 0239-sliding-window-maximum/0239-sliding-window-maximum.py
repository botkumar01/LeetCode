from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        st = deque()
        for i in range(len(nums)):
            if i >= k-1:
                while st and nums[st[-1]] <nums[i]:
                    st.pop()
                else:
                    st.append(i)
                while i - st[0] >= k:
                    st.popleft()
                ans.append(nums[st[0]])
            else:
                while st and nums[st[-1]] < nums[i]:
                    st.pop()
                st.append(i)
        return ans