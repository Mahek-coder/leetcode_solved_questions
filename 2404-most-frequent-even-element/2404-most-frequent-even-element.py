class Solution(object):
    def mostFrequentEven(self, nums):
        listt,dict1=[],{}
        for i in nums:
            if(i%2==0):
                listt.append(i)
        if(len(listt)==0):
            return -1
        listt.sort()  

        for i in listt:
            dict1[i]=dict1.get(i,0)+1
        max_count=max(dict1.values())
        ans=float('inf')

        for i in dict1:
            if(dict1[i]==max_count):
                ans=min(ans,i)  
        return ans            