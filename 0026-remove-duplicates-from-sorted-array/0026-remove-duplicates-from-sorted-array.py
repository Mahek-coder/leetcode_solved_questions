class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listt=[]
        for i in nums:
            if i not in listt:
                listt.append(i)
        for i in range(len(listt)):
            nums[i]=listt[i]        
        return len(listt)        