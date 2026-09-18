class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        listt=[]
        if n==1:
            listt.append(0)
            return listt
        if n%2==0:
            for i in range(1,(n//2)+1):
                 listt.append(i)
                 listt.append(-i)
        else:
            listt.append(0)
            for i in range(1,(n//2)+1):
                 listt.append(i)
                 listt.append(-i) 
        listt.sort()
        return listt                