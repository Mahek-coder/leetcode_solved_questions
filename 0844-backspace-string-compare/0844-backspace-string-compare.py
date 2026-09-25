class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        listt1,listt2=[],[]
        for i in range(len(s)):
            if s[i]=='#':
                if(len(listt1)>0):
                   listt1.pop()
            else:
                listt1.append(s[i])
        for i in range(len(t)):
            if t[i]=='#':
                if(len(listt2)>0):
                   listt2.pop()
            else:
                listt2.append(t[i])
        return listt1==listt2