class Solution(object):
    def mergeAlternately(self, word1, word2):
        res=[]
        if(len(word1)>=len(word2)):
            join=word1
        else:
            join=word2    
        for i in range(len(join)):
             if(len(word1)>i):
                 res.append(word1[i])
             if(len(word2)>i):
                 res.append(word2[i]) 
        return "".join(res)    