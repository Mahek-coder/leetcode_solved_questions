class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        listt1,listt2,rank,dict1=[],[1],1,{}
        listt1=list(arr)
        listt1.sort()
        for i in range(1,len(listt1)):
             if i>0 and listt1[i]!=listt1[i-1]:
                 rank+=1
             listt2.append(rank)
        rank=[]
        for i in range(len(listt1)):
            dict1[listt1[i]]=listt2[i]
        for i in arr:
            rank.append(dict1[i])
        return rank