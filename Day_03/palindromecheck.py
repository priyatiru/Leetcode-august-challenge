class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()   #Converts string to lower
        x = ''
        for i in s:
            if i.isalnum():   # Checks if string is alphanumeric
                x+=(i)
        return x==x[::-1]