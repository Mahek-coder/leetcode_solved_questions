class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        listt1,listt2,min_diff=[],[],[]
        arr.sort()
        for i in range(len(arr)-1):
             listt1.append(arr[i+1]-arr[i])
             listt2.append([arr[i],arr[i+1]])
        mini=min(listt1)
        for i in range(len(listt1)):
             if(listt1[i]==mini):
                min_diff.append(listt2[i])
        return min_diff