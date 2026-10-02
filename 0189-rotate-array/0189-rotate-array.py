class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        listt1,listt2=[],[]
        k=k%len(nums)
        if(k==0):
            return nums
        for i in range(k):
            listt1.append(nums[-1])
            nums.pop()
            if(len(listt1)==k):
                break
        listt1.reverse()
        listt2=nums.copy()
        for i in range(len(listt1)):
            nums.append(0)
        for i in range(len(nums)):
            if(i<k):
                nums[i]=listt1[i]
            else:
                nums[i]=listt2[i-k]