class Solution(object):
    def findKthLargest(self, nums, k):
        listt=list(nums)
        listt.sort(reverse=True)
        return listt[k-1]