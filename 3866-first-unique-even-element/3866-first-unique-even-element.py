class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listt=[]
        for i in nums:
            if(i%2==0):
                if(nums.count(i)==1):
                    return i       
        return -1                        