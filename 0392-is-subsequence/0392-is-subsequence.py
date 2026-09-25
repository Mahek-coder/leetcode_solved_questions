class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        strr,count="",0
        if(len(s)==0):
            return True
        for i in range(0,len(t)):
            if(s[count]==t[i]):
                strr+=t[i]
                count+=1
            if(count==len(s)):
                break
        return strr==s