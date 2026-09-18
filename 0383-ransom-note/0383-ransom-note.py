class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        listt=list(magazine)
        if(len(ransomNote)>len(magazine)):
            return False
        for i in ransomNote:
            if i in listt:
                 listt.remove(i)
            else:
                return False     
        return True