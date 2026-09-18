class Solution(object):
    def findWords(self, words):
        listt=[]
        for i in words:
            count1,count2,count3=0,0,0
            for j in i:
                if j in "aAsSdDfFgGhHjJkKlL":
                    count1+=1
                elif j in "qwertyuiopQWERTYUIOP":
                    count2+=1    
                elif j in "zxcvbnmZXCVBNM":
                    count3+=1   
            if(count1==len(i) or count2==len(i) or count3==len(i)):
                listt.append(i) 
        return listt                            