'''
Pascals triangle - Triangular array of binomial coefficient

Idea of the solution written- summing adjacent elements in preceeding rows
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        arr=[[1],[1,1]]
        k=1
        for i in range(2,n+1):
            arr.append([])
            arr[i].append(1)
            for j in range(1,k+1):
                arr[i].append(arr[i-1][j-1]+arr[i-1][j])
            k+=1
            arr[i].append(1)
        return arr[n]