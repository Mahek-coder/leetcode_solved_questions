class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result=""
        for i in range(len(s)):
            for j in range(len(indices)):
                if indices[j]==i:
                    result+=s[j] 
        return result 