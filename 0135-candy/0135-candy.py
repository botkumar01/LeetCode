class Solution(object):
    def candy(self, r):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = [1]
        last = 1
        prev = r[0]
        anss = 0
        n = len(r)
        for i in range(n-1):
            if r[i] > prev:
                ans.append(ans[-1] + 1 )
            elif r[i] > r[i+1]:
                ans.append(2)
            else:
                ans.append(1)
            prev = r[i]
        
        if r[n-1] > prev:
            ans.append(ans[-1] + 1 )
        else:
            ans.append(1)
        end=len(r)-1
        k = len(ans)-1
        while k > 0:
            if r[end] < r[end - 1]:
                if ans[k - 1] <= ans[k]:
                    ans[k - 1] = ans[k] + 1

            anss += ans[k]
            k-=1
            end-=1
        ans = []
        return anss
