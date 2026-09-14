class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        val,listt=max(candies),[]
        for i in candies:
            if(i+extraCandies>=val):
                listt.append(True)
            else:
                listt.append(False)
        return listt            
