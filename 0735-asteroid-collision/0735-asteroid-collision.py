class Solution(object):
    def asteroidCollision(self, nums):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st = []
        ans = []
        a = len(nums)-1
        while a >= 0:
            if nums[a] >= 0 and len(st) == 0:
                ans .append(nums[a])
                a-=1
            elif nums[a] <0:
                st.append(nums[a])
                print st
                a-=1
            else:
                while len(st) != 0 and nums[a] >=0 and a>=0:
                    if nums[a] > -(st[-1]):
                        st.pop()
                    elif nums[a] == -(st[-1]):
                        a-=1
                        st.pop()
                    else:
                        a-=1
                if a>= 0 and nums[a] >=0:
                    ans.append(nums[a])
                    a-=1
        for i in st:
            ans.append(i)
        # print st
        return ans[::-1]