class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        listt=[]
        val=s.split()
        for j in range(1,len(val)+1):
            for i in val:
                 if int(i[-1])==j:
                    listt.append(i[:-1])
        return " ".join(listt) 