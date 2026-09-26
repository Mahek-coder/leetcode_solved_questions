class Solution(object):
    def removeDuplicates(self, s):
        listt=[]
        for i in s:
            if len(listt)>0 and listt[-1]==i:
                listt.pop()
            else:
                listt.append(i)
        return "".join(listt)