class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        listt=[]
        for i in operations:
            if(i=='C'):
                listt.pop()
            elif(i=='D'):
                listt.append(listt[-1]*2)
            elif(i=='+'):
                listt.append(listt[-1]+listt[-2])
            else:
                listt.append(int(i))
        return sum(listt)