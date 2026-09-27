class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        listt=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                 if(nums1[i]==nums2[j] and j==len(nums2)-1):
                    listt.append(-1)
                 elif(nums1[i]==nums2[j]):
                    right=nums2[j+1:]
                    for K in right:
                        if(nums2[j]<K):
                            listt.append(K)
                            break
                    else:
                        listt.append(-1)
        return listt