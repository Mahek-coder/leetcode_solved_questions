class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count1,count2=0,0
        for i in nums:
            if(i<=-1):
                count1+=1
            elif(i>=1):
                count2+=1    
        return max(count1,count2)        