class Solution(object):
    def candy(self, r):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = []
        last = 1
        prev = r[0]
        anss = 0
        for i in range(len(r)):
            if i != 0 and r[i] > prev:
                ans.append(ans[-1] + 1 )
                # last = last+1
                # anss+=last
            elif i !=len(r)-1 and r[i] > r[i+1]:
                ans.append(2)
                # last = 2
                # anss += 2
            else:
                ans.append(1)
                # last = 1
                # anss += 1
            prev = r[i]
       
        # if r[len(r)-1] >prev:
        #     ans.append(ans[-1] + 1 )
        # else:
        #     ans.append(1)
        end=len(r)-1
        
        for i in range(1,len(r)):
            if r[end] < r[end-1]:
                if ans[end] >= ans[end-1]:
                    # anss -= ans[end-1]
                    ans[end-1] = ans[end] +1

                    # anss += ans[end-1]
            anss += ans[end]
            end-=1
        anss += ans[0]
        # return sum(ans)
        return anss
