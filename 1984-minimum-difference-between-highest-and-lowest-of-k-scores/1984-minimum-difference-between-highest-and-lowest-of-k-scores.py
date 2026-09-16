class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        listt=[]
        if(k>len(nums)):
            return -1
        for i in range(len(nums)+1-k):
             val=nums[(i+k)-1]-nums[i]
             listt.append(val)
        return min(listt)     