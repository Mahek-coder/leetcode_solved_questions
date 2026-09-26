class Solution(object):
    def isValid(self, s):
        open_brak="({["
        listt=[]
        for i in range(len(s)):
            if s[i] in open_brak:
                 listt.append(s[i])
            else:
                 if(len(listt)==0):
                    return False
                 if s[i]==')' and listt[-1]=='(':
                    listt.pop()
                 elif s[i]=='}' and listt[-1]=='{':
                    listt.pop()
                 elif s[i]==']' and listt[-1]=='[':
                    listt.pop()
                 else:
                    return False
        return len(listt)==0