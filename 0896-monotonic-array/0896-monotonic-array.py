class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1=nums[:]
        nums2=nums[:]
        nums1.sort()
        nums2.sort(reverse=True)
        if(nums1==nums):
           return True
        elif(nums2==nums):
           return True
        return False         