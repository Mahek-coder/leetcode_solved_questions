class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in s:
            res=res+i.lower()
        return res    