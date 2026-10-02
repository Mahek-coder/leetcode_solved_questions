class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        listt=[]
        for i in range(1,n+1):
            listt.append("Push")
            if i not in target:
                listt.append("Pop")
            if(target[-1]==i):
                return listt
        