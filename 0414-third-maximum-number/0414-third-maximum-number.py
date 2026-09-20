class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listt=[]
        listt=list(set(nums))
        listt.sort(reverse=True)
        if(len(listt)<3):
            return listt[0]
        return listt[2]