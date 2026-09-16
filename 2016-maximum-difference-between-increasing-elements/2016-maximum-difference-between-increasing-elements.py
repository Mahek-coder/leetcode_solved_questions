class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listt=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    listt.append(nums[j]-nums[i])
        if(len(listt)==0):
            return -1            
        return max(listt)            