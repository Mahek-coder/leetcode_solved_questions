class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        listt=[]
        for i in tokens:
            if i=='+':
                val1=listt.pop()
                val2=listt.pop()
                listt.append(int(val2)+int(val1))
                val1,val2=0,0
            elif i=='*':
                val1=listt.pop()
                val2=listt.pop()
                listt.append(int(val2)*int(val1))
                val1,val2=0,0
            elif i=='/':
                val1=listt.pop()
                val2=listt.pop()
                listt.append(int(val2/val1))
                val1,val2=0,0
            elif i=='-':
                val1=listt.pop()
                val2=listt.pop()
                listt.append(int(val2)-int(val1))
                val1,val2=0,0
            else:
                listt.append(int(i))
        return listt[-1]