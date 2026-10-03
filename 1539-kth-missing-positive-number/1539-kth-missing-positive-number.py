class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        listt=[]
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                listt.append(i)
        return listt[k-1]