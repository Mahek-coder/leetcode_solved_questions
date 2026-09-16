class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U,D,L,R=1,-1,100,-100
        store=0
        if(len(moves)%2!=0):
            return False  
        for i in range(len(moves)):
            if(moves[i]=="U"):
                store+=U
            elif(moves[i]=="D"):
                store+=D
            elif(moves[i]=="L"):
                store+=L
            else:
                store+=R        
        if(store==0):
            return True
        return False        
