class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        listt=[]
        for i in nums:
            temp=[]
            while(i>0):
                sep=i%10
                temp.append(sep)
                i//=10
            temp.reverse()
            listt.extend(temp)
        return listt        