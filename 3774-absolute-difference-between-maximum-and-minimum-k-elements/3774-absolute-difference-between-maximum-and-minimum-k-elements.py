class Solution(object):
    def absDifference(self, nums, k):
        sum1,sum2,diff=0,0,0
        nums.sort()
        for i in range(k):
            sum1+=nums[i]
            sum2+=nums[len(nums)-i-1]
        return abs(sum1-sum2)