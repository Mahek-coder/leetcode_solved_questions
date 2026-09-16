class Solution(object):
    def majorityElement(self, nums):
       dict1={}
       for i in nums:
           dict1[i]=dict1.get(i,0)+1
       for i in nums:
           if (len(nums)/2)<dict1[i]: 
               return i   