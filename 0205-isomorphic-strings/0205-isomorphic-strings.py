class Solution(object):
    def isIsomorphic(self, s, t):
        dict1,dict2,listt1,listt2={},{},[],[]
        count=0
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            dict1[s[i]]=t[i]
        for i in s:
            listt1.append(dict1[i])
        if (listt1==list(t)):
            count+=1
        for i in range(len(s)):
            dict2[t[i]]=s[i]
        for i in t:
            listt2.append(dict2[i])
        if (listt2==list(s)):
            count+=1
        return count==2