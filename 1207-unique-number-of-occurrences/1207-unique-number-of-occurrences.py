class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict1={}
        for i in arr:
            dict1[i]=dict1.get(i,0)+1
        listt=list(dict1.values())
        listt.sort()
        for i in range(len(listt)-1):
            if listt[i]==listt[i+1]:
                return False    
        return True        