class Solution:
    def numsSameConsecDiff(self, N: int, k: int) -> List[int]:
        if(N==1):
            return list(range(10))
        
        if(N==0):
            return list(range(1,10))
        
        ml=[i for i in range(1,10) if(i+k<10 or i-k>=0)]
        
        res=[]
        
        for j in range(1,N):
            res=[]
            for i in range(len(ml)):

                if(ml[i]%10+k in range(1,10)):      
                    res+=[ml[i]*10+(ml[i]%10+k)]

                if(ml[i]%10-k in range(0,10)):
                    res+=[ml[i]*10+(ml[i]%10-k)]

            ml=list(set(res))

        return(ml)