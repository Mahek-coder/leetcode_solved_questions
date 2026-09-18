class Solution(object):
    def findRestaurant(self, list1, list2):
        list_common,list_index,list_ans=[],[],[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i]==list2[j]):
                    list_common.append(list1[i])
                    add=i+j
                    list_index.append(add)
        val=min(list_index)

        for i in range(len(list_index)):
            if(list_index[i]==val):
                list_ans.append(list_common[i])
        return list_ans                                    