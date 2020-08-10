class Solution:
    def titleToNumber(self, s):
        output=0
        for i in range(len(s)):
            output+=26**(len(s)-i-1) * (ord(s[i])-ord('A') + 1)
        return output


#################################################################
"""
EXAMPLE: i/p: AB , o/p: 28
len(s)=2
for i =0:
    26**(2-0-1)*(1-1+1)    here ord(A)=1 , ord() function returns the number representing the unicode code of a specified character.
    = 26
for i =1:
    26**(2-1-1)*(2-1+1)   here ord(B)=2
    =2

output= 28

"""
#################################################################




  