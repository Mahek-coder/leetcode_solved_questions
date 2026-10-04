class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        listt=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                listt.append(i)
        return listt