class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        count=0
        if (num and(not (num &(num-1)))):
            while (num>1):
                num>>=1
                count+=1
            if(count%2==0):
                return True
            else:
                return False