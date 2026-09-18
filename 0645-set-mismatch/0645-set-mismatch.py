class Solution(object):
    def findErrorNums(self, nums):
        listt,listt1=[],[]
        for i in nums:
             if i in listt1:
                listt.append(i)
                break
             else:
                listt1.append(i) 
        nums.sort()        
        for i in range(1,len(nums)+1):
            if(i!=nums[i-1]):
                if(i==len(nums)):
                    listt.append(i)
                    break
                elif(i==nums[i]):
                   continue
                else:    
                   listt.append(i)
                   break
        return  listt        