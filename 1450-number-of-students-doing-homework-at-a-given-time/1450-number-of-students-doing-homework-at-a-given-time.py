class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        listt1,listt2,count=[],[],0
        if(len(startTime)<len(endTime)):
            val=len(startTime)
        else:
            val=len(endTime)
        for i in range(val):
            if(startTime[i]<=queryTime and endTime[i]>=queryTime):
                 count+=1
        return count