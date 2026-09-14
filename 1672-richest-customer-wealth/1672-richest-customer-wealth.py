class Solution(object):
    def maximumWealth(self, accounts):
       listt=[]
       for i in accounts:
          max_val=0
          for j in i:
             max_val+=j
          listt.append(max_val)  
       return max(listt)    