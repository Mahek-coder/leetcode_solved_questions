class Solution(object):
    def reverseVowels(self, s):
        left,vowels=0,"aeiouAEIOU"
        listt=list(s)
        right=len(s)-1
        while(left<right):
             if s[left] in vowels and s[right] in vowels:
                listt[left]=s[right]
                listt[right]=s[left]
                right-=1
                left+=1 
             elif s[left] in vowels:
                right-=1
             elif s[right] in vowels:
                left+=1 
             else:
                right-=1
                left+=1 
        return "".join(listt)     