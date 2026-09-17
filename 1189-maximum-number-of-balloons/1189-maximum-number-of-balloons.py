class Solution(object):
    def maxNumberOfBalloons(self, text):
        dict1,count={},0
        for i in text:
            dict1[i]=dict1.get(i,0)+1
        while(len(dict1)!=0):  
            possible=True  
            for i in "balloon":
                if i in dict1:
                    dict1[i]-=1
                    if(dict1[i]==0):
                        del dict1[i]
                else:
                    possible=False
                    break 
            if(possible==False):
                break        
            count+=1     
        return count           