class Solution(object):
    def maxProductDifference(self, nums):
        listt=[]
        listt=list(nums)
        listt.sort(reverse=True)
        val=((listt[0]*listt[1])-(listt[len(listt)-1]*listt[len(listt)-2]))
        return val