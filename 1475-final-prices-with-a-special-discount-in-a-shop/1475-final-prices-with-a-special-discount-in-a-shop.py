class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        listt=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                 if(prices[i]>=prices[j]):
                     listt.append(prices[i]-prices[j])
                     break
            else:
                listt.append(prices[i])
        return listt