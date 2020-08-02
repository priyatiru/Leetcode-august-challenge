class Solution(object):
    def detectCapitalUse(self, word):
        first_cap = word[0].isupper()  # judge if first character is capital
        cap  = 0 # count capital char
        n = len(word) 
        for i in range(n):
            if word[i].isupper(): # count capital char
                cap += 1
            if first_cap == True: # if first is capital, the cap should be 1 or i + 1.
                if cap != 1 and cap != i + 1:
                    return False
            elif cap != 0: # if first is not capital, cap should be 0.
                return False
        return True