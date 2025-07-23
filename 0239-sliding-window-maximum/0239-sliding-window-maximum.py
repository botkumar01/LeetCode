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
            while st and i - st[0] >= k:
                st.popleft()
            while st and nums[st[-1]] <nums[i]:
                st.pop()
            st.append(i)
            if i >= k-1:
                ans.append(nums[st[0]])
            
        return ans