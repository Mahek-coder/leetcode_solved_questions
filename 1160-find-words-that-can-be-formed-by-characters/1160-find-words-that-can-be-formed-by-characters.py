class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        add=0
        for i in words:
            listt=list(chars)
            count=0
            for j in i:
                 if j in listt:
                     listt.remove(j)
                     count+=1
                 else:
                    break    
                 if(count==len(i)):
                     add+=count 
        return add                    