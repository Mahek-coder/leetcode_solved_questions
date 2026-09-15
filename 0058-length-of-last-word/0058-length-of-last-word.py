class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        listt=s.split()
        count=0
        for i in listt[-1]:
            count+=1
        return count    