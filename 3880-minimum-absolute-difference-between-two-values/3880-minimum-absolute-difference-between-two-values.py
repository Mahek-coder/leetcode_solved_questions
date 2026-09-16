class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listt=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                 if(nums[i]==1 and nums[j]==2):
                      listt.append(abs(i-j))
        if(len(listt)==0):
            return -1
        return min(listt)     
         