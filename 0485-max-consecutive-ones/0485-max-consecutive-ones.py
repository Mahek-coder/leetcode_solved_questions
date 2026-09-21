class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        listt,count=[],0
        if 0 not in nums:
            return len(nums)
        if 1 not in nums:
            return 0
        for i in range(len(nums)):
            if(nums[i]==1):
                count+=1
            else:
                listt.append(count)
                count=0
        listt.append(count)
        return max(listt)