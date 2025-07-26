class Solution(object):
    def findContentChildren(self, g, s):
        # hashi = {}
        # for i in s:
        #     hashi[i] = hashi.get(i,0)+1
        # ans,maxi =0,0
        # hashii = {}
        # for i in g:
        #     hashii[i] = hashii.get(i,0)+1
        # for i in hashi:
        #     if i in hashii:
        #         j = hashi[i] - hashii[i]
        #         if  j >= 0:
        #             ans += (hashi[i]- j)
        #         else:
        #             ans += (j + hashi[i])
        # return ans
        g = sorted(g)
        s=sorted(s)
        ans = 0
        point_g = 0
        point_s = 0
        while point_g <len(g) and point_s < len(s) :
            if g[point_g] <= s[point_s]:
                ans+=1
                point_g +=1
                point_s +=1
            else:
                while point_s < len(s) and g[point_g] > s[point_s]:
                    point_s +=1
        return ans