class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1={}
        for i in s:
            dict1[i]=dict1.get(i,0)+1
        for i in range(len(s)):
            if(dict1[s[i]]==1):
                return i
        return -1        