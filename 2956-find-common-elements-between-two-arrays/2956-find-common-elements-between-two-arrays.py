class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count,listt=0,[]
        for i in nums1:
            if i in nums2:
                count+=1
        listt.append(count)
        count=0
        for i in nums2:
            if i in nums1:
                count+=1
        listt.append(count)
        return listt