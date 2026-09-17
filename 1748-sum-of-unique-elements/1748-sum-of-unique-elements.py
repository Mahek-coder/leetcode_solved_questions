class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        dict1={}
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
        for i in dict1:
            if(dict1[i]==1):
                sum1+=i   
        return sum1        