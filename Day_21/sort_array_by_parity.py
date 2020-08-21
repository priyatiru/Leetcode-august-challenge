'''
In place swapping. 
i= elements in array A
j= count of odd elements
'''


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j=0
        for i in range(len(A)):
            if (A[i]%2)==0:
                temp = A[i]
                A[i]=A[j]
                A[j]=temp
                j+=1
        return A