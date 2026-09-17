import string
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for p in string.punctuation:
            paragraph=paragraph.replace(p," ")
        dict1={}
        para1=paragraph.split()
        for i in para1:
            dict1[i.lower()]=dict1.get(i.lower(),0)+1
        for i in banned:
            if i in dict1:
                 del dict1[i]   
        return max(dict1,key=dict1.get)