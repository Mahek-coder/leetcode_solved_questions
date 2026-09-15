class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count,listt=0,[]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(arr[i]==arr[j]):
                    count+=1
            if(count==arr[i]):
                listt.append(arr[i])
            count=0
        if(len(listt)==0):
            return -1
        else:
            return max(listt)     
