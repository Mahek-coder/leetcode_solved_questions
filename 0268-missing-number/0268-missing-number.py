class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        count=0
        for i in range(len(nums)):
            if count==nums[i]:
                count+=1
            else:
                return count
        return count