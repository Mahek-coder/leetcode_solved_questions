class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        listt=[]
        for i in s:
            if i.isdigit():
                listt.append(int(i))
        listt=list(set(listt))
        listt.sort(reverse=True)
        if(len(listt)<2):
            return -1
        return listt[1]