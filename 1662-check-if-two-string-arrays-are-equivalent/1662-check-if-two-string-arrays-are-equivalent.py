class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1="".join(word1)
        word2="".join(word2)
        count=0
        if(len(word1)!=len(word2)):
            return False
        for i in range(0,len(word1)):
            if(word1[i]==word2[i]):
                  count+=1
        return count==len(word1)     