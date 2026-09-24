class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            sum1,val=0,nums[i]
            while(val>0):
                digit=val%10
                sum1+=digit
                val//=10
            if(sum1==i):
                return i
        return -1