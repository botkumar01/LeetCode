class Solution(object):
    def numberOfSubstrings(self, nums):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        aa =0 
        bb=0
        cc=0
        a=[]
        b = []
        c = []
        for i in range(len(nums)):
            if nums[i] == "a":
                a.append(i)
            elif nums[i] == "b":
                b.append(i)
            else:
                c.append(i)
        for i in nums:
            if aa>=len(a) or  bb>=len(b) or  cc>=len(c):
                break
            end = max(a[aa],b[bb],c[cc])
            cnt += len(nums)-end
            if i =='a':
                aa+=1
            elif i=='b':
                bb+=1
            else:
                cc+=1

            
            
        return cnt
        # for i in range(len(nums)-2):
        #     a = False
        #     b=False
        #     c = False
        #     for j in range(i,len(nums)):
        #         if nums[j] == "a":
        #             a = True
        #         elif nums[j] == "b":
        #             b = True
        #         else:
        #             c =True
        #         if a==True and b ==True and c ==True:
        #             cnt += len(nums)-j
        #             break
        # return cnt
    