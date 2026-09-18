class Solution(object):
    def isTrionic(self, nums):
        listt=[]
        for i in range(len(nums)):
            if(i+1!=len(nums) and nums[i]<nums[i+1]):
                listt.append(nums[i]) 
            else: 
                if(len(listt)>0):
                   listt.append(nums[i])
                else:
                    return False      
                break      
        if(len(listt)==len(nums)):
            return False        
        for i in range(len(listt)-1,len(nums)):
            if(i+1!=len(nums) and nums[i]>nums[i+1]):
                listt.append(nums[i+1])    
            else:
                break   
        if(len(listt)==len(nums)):
            return False                 
        for i in range(len(listt)-1,len(nums)):
            if(i+1!=len(nums) and nums[i]<nums[i+1]):
                listt.append(nums[i+1]) 
            else:
                break      
        return listt==nums        