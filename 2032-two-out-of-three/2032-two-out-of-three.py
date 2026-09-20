class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        listt=[]
        set1=set(nums1)
        set2=set(nums2)
        set3=set(nums3)
        set_inter1=set1.intersection(set2)
        set_inter2=set3.intersection(set2)
        set_inter3=set1.intersection(set3)
        set_union1=set_inter1.union(set_inter2)
        set_union2=set_union1.union(set_inter3)
        listt=list(set_union2)
        return listt   