class Solution(object):
    def flipAndInvertImage(self, image):
        listt,val=[],0
        for i in image:
            for j in i:
                if(j==1):
                    listt.append(0)
                else:
                    listt.append(1)
        matrix=[[0]*len(image[0]) for i in range(len(image))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                matrix[i][len(image[0])-1-j]=listt[val]
                val+=1
        return matrix