class Solution(object):
    def merge(self, arr):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        cnt = 0
        if len(arr)<=1:
            return arr
        ans = []
        arr.sort()
        # print(arr)
        a = arr[0][0]
        b = arr[0][1]
        for i in range(1,len(arr)):
            if b >= arr[i][0]:
                b = max(b,arr[i][1])
            else:
                # cnt +=1
                ans.append([a,b])
                a = arr[i][0]
                b = arr[i][1]
        ans.append([a,b])
        return(ans)
        arr.sort()
        ans = []
        p = 0
        l=0
        while p < len(arr)-1:
            add = []
            add.append(arr[p][0])
            m=arr[p][1]
            # if p==len(arr)-1:
            #     ans.append(arr[p])
            #     break
            while p<len(arr)-1 and m>= arr[p+1][0]:
                m  = max(m,arr[p+1][1])
                p+=1
            add.append(m)
            ans.append(add)
            p+=1
        if p==len(arr)-1:
            ans.append(arr[p])
        return ans
        # ans = [[arr[0]]]
        # p=0
        # for i in range(len(arr)-1):
        #     while p < len(arr) and arr[p][0]>:
        #         p+=1
            
        # return ans